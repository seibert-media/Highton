from highton import (
    fields,
    call_mixins,
)
from highton.highton_constants import HightonConstants
from highton.models.contact import Contact


class Person(
    Contact,
    call_mixins.ListCallMixin,
    call_mixins.CreateCallMixin,
    call_mixins.DetailCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DeleteCallMixin,
    call_mixins.ListNoteCallMixin,
    call_mixins.ListEmailCallMixin,
    call_mixins.ListTagCallMixin,
    call_mixins.ListTaskCallMixin,
    call_mixins.CreateTagCallMixin,
    call_mixins.CreateNoteCallMixin,
    call_mixins.DeleteTagCallMixin,
    call_mixins.SearchCallMixin,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar company_id: fields.IntegerField(name=HightonConstants.COMPANY_ID)
    :ivar company_name: fields.StringField(name=HightonConstants.COMPANY_NAME)
    :ivar first_name: fields.StringField(name=HightonConstants.FIRST_NAME)
    :ivar last_name: fields.StringField(name=HightonConstants.LAST_NAME)
    :ivar title: fields.StringField(name=HightonConstants.TITLE)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar background: fields.StringField(name=HightonConstants.BACKGROUND)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar group_id: fields.IntegerField(name=HightonConstants.GROUP_ID)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar visible_to: fields.StringField(name=HightonConstants.VISIBLE_TO)
    :ivar linkedin_url: fields.StringField(name=HightonConstants.LINKEDIN_URL)
    :ivar avatar_url: fields.StringField(name=HightonConstants.AVATAR_URL)
    :ivar tags: fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
    :ivar contact_data: fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
    :ivar subject_datas: fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)
    """
    ENDPOINT = HightonConstants.PEOPLE
    TAG_NAME = HightonConstants.PERSON
    OFFSET = 500

    def __init__(self, **kwargs):
        self.company_id = fields.IntegerField(name=HightonConstants.COMPANY_ID, required=True)
        self.company_name = fields.StringField(name=HightonConstants.COMPANY_NAME, required=True)
        self.first_name = fields.StringField(name=HightonConstants.FIRST_NAME, required=True)
        self.last_name = fields.StringField(name=HightonConstants.LAST_NAME, required=True)
        self.title = fields.StringField(name=HightonConstants.TITLE, required=True)

        super().__init__(**kwargs)

    @classmethod
    def list(cls, page=0, since=None, tag_id=None, title=None):
        """

        :param page: page starting by 0
        :type page: int
        :param since:
        :type since: datetime.datetime
        :param tag_id: id of a tag
        :type tag_id: int
        :param title:
        :type title: str
        :return: list of person objects
        :rtype: list
        """
        params = {}
        if page:
            params['n'] = int(page) * cls.OFFSET
        if since:
            params['since'] = since.strftime(cls.COLLECTION_DATETIME)
        if tag_id:
            params['tag_id'] = str(tag_id)
        if title:
            params['title'] = title

        return super().list(params)
