from highton import call_mixins
from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class User(
    HightonModel,
    call_mixins.ListCallMixin,
    call_mixins.DetailCallMixin,
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    :ivar email_address: fields.StringField(name=HightonConstants.EMAIL_ADDRESS)
    :ivar admin: fields.BooleanField(name=HightonConstants.ADMIN)
    :ivar token: fields.StringField(name=HightonConstants.TOKEN)
    :ivar dropbox: fields.StringField(name=HightonConstants.DROPBOX)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    """
    ENDPOINT = HightonConstants.USERS
    TAG_NAME = HightonConstants.USER

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME)
        self.email_address = fields.StringField(name=HightonConstants.EMAIL_ADDRESS)
        self.admin = fields.BooleanField(name=HightonConstants.ADMIN)
        self.token = fields.StringField(name=HightonConstants.TOKEN)
        self.dropbox = fields.StringField(name=HightonConstants.DROPBOX)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)

        super().__init__(**kwargs)

    @classmethod
    def me(cls):
        """
        Returns information about the currently authenticated user.

        :return:
        :rtype: User
        """
        return fields.ObjectField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/me').text
            )
        )
