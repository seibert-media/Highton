from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields
from highton import call_mixins


class Task(
    HightonModel,
    call_mixins.CreateCallMixin,
    call_mixins.DetailCallMixin,
    call_mixins.DeleteTagCallMixin,
    call_mixins.UpdateCallMixin,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar recording_id: fields.IntegerField(name=HightonConstants.RECORDING_ID)
    :ivar subject_id: fields.IntegerField(name=HightonConstants.SUBJECT_ID)
    :ivar subject_type: fields.StringField(name=HightonConstants.SUBJECT_TYPE)
    :ivar subject_name: fields.StringField(name=HightonConstants.SUBJECT_NAME)
    :ivar category_id: fields.IntegerField(name=HightonConstants.CATEGORY_ID, required=True)
    :ivar body: fields.StringField(name=HightonConstants.BODY, required=True)
    :ivar frame: fields.StringField(name=HightonConstants.FRAME, required=True)
    :ivar due_at: fields.DatetimeField(name=HightonConstants.DUE_AT, required=True)
    :ivar alert_at: fields.DatetimeField(name=HightonConstants.ALERT_AT)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar public: fields.BooleanField(name=HightonConstants.PUBLIC)
    :ivar recurring_period: fields.StringField(name=HightonConstants.RECURRING_PERIOD)
    :ivar anchor_type: fields.IntegerField(name=HightonConstants.ANCHOR_TYPE)
    :ivar done_at: fields.DatetimeField(name=HightonConstants.DONE_AT)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    """
    TAG_NAME = HightonConstants.TASK
    ENDPOINT = HightonConstants.TASKS

    def __init__(self, **kwargs):
        self.recording_id = fields.IntegerField(name=HightonConstants.RECORDING_ID)
        self.subject_id = fields.IntegerField(name=HightonConstants.SUBJECT_ID)
        self.subject_type = fields.StringField(name=HightonConstants.SUBJECT_TYPE)
        self.subject_name = fields.StringField(name=HightonConstants.SUBJECT_NAME)
        self.category_id = fields.IntegerField(name=HightonConstants.CATEGORY_ID, required=True)
        self.body = fields.StringField(name=HightonConstants.BODY, required=True)
        self.frame = fields.StringField(name=HightonConstants.FRAME, required=True)
        self.due_at = fields.DatetimeField(name=HightonConstants.DUE_AT, required=True)
        self.alert_at = fields.DatetimeField(name=HightonConstants.ALERT_AT)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.public = fields.BooleanField(name=HightonConstants.PUBLIC)
        self.recurring_period = fields.StringField(name=HightonConstants.RECURRING_PERIOD)
        self.anchor_type = fields.IntegerField(name=HightonConstants.ANCHOR_TYPE)
        self.done_at = fields.DatetimeField(name=HightonConstants.DONE_AT)
        self.owner_id = fields.IntegerField(name=HightonConstants.OWNER_ID)

        super().__init__(**kwargs)

    def complete(self):
        """
        Complete current task
        :return:
        :rtype: requests.models.Response
        """
        return self._post_request(
            data='',
            endpoint=self.ENDPOINT + '/' + str(self.id) + '/complete'
        )

    @classmethod
    def list_upcoming(cls):
        """
        Returns a collection of upcoming tasks (tasks that have not yet been completed,
        regardless of whether they’re overdue) for the authenticated user

        :return:
        :rtype: list
        """
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/upcoming').text
            )
        )

    @classmethod
    def list_assigned(cls):
        """
        Returns a collection of upcoming tasks (tasks that have not yet been completed,
        regardless of whether they’re overdue) that were created by the authenticated user,
        but assigned to somebody else.

        :return:
        :rtype: list
        """
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/assigned').text
            )
        )

    @classmethod
    def list_completed(cls):
        """
        Returns a collection of completed tasks.

        :return:
        :rtype: list
        """
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/completed').text
            )
        )

    @classmethod
    def list_today(cls):
        """
        Returns a collection of uncompleted tasks due for the rest of today for the authenticated user.

        :return:
        :rtype: list
        """
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/today').text
            )
        )

    @classmethod
    def list_all(cls):
        """
        Returns a collection of all tasks visible to the current user.

        :return:
        :rtype: list
        """
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/all').text
            )
        )
