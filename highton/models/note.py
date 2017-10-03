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
    call_mixins.ListCommentCallMixin,
):
    """

    :ivar id: fields:IntegerField(name=HightonConstants.ID)
    :ivar body: fields.StringField(name=HightonConstants.BODY, required=True)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar subject_id: fields.IntegerField(name=HightonConstants.SUBJECT_ID, required=True)
    :ivar subject_type: fields.StringField(name=HightonConstants.SUBJECT_TYPE, required=True)
    :ivar subject_name: fields.StringField(name=HightonConstants.SUBJECT_NAME)
    :ivar collection_id: fields.IntegerField(name=HightonConstants.COLLECTION_ID)
    :ivar collection_type: fields.StringField(name=HightonConstants.COLLECTION_TYPE)
    :ivar visible_to: fields.StringField(name=HightonConstants.VISIBLE_TO)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    :ivar group_id: fields.IntegerField(name=HightonConstants.GROUP_ID)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar attachments: fields.ListField(name=HightonConstants.ATTACHMENTS, init_class=Attachment)
    """
    TAG_NAME = HightonConstants.NOTE
    ENDPOINT = HightonConstants.NOTES

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
