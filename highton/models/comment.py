from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields
from highton import call_mixins


class Comment(
    HightonModel,
    call_mixins.DetailCallMixin,
    call_mixins.CreateCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DeleteCallMixin,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar parent_id: fields.IntegerField(name=HightonConstants.PARENT_ID)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar body: fields.StringField(name=HightonConstants.BODY)

    """
    TAG_NAME = HightonConstants.COMMENT
    ENDPOINT = HightonConstants.COMMENTS

    def __init__(self, **kwargs):
        self.parent_id = fields.IntegerField(name=HightonConstants.PARENT_ID, required=True)
        self.body = fields.StringField(name=HightonConstants.BODY, required=True)
        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)

        super().__init__(**kwargs)
