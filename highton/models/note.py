from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import (
    fields,
    call_mixins,
)
from highton.models.attachment import Attachment


class Note(
    HightonModel,
    call_mixins.DetailCallMixin,
    call_mixins.CreateCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DeleteCallMixin,
):
    """

    :ivar id: fields:IntegerField(name=HightonConstants.ID)
    :ivar location: fields.StringField(name=HightonConstants.LOCATION)
    :ivar address: fields.StringField(name=HightonConstants.ADDRESS)
    :ivar protocol: fields.StringField(name=HightonConstants.PROTOCOL)
    """
    TAG_NAME = HightonConstants.NOTE

    def __init__(self, **kwargs):
        self.body = fields.StringField(name=HightonConstants.BODY, required=True)
        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.subject_id = fields.IntegerField(name=HightonConstants.SUBJECT_ID, required=True)
        self.subject_type = fields.StringField(name=HightonConstants.SUBJECT_TYPE, required=True)
        self.subject_name = fields.StringField(name=HightonConstants.SUBJECT_NAME)
        self.collection_id = fields.IntegerField(name=HightonConstants.COLLECTION_ID)
        self.collection_type = fields.StringField(name=HightonConstants.COLLECTION_TYPE)
        self.visible_to = fields.StringField(name=HightonConstants.VISIBLE_TO)
        self.owner_id = fields.IntegerField(name=HightonConstants.OWNER_ID)
        self.group_id = fields.IntegerField(name=HightonConstants.GROUP_ID)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.attachments = fields.ListField(name=HightonConstants.ATTACHMENTS, init_class=Attachment)

        super().__init__(**kwargs)
