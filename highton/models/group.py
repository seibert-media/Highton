from highton import call_mixins
from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class Group(
    HightonModel,
    call_mixins.ListCallMixin,
    call_mixins.DetailCallMixin,
    call_mixins.CreateCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DeleteCallMixin,
):
    """
    The authenticated user needs to be an administrator to perform these actions.

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    :ivar users: fields.ListField(name=HightonConstants.USERS, init_class=models.User)
    """
    ENDPOINT = HightonConstants.GROUPS
    TAG_NAME = HightonConstants.GROUP

    def __init__(self, **kwargs):
        from highton import models

        self.name = fields.StringField(name=HightonConstants.NAME)
        self.users = fields.ListField(name=HightonConstants.USERS, init_class=models.User)

        super().__init__(**kwargs)
