from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class SubjectData(
    HightonModel,
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar value: fields.StringField(name=HightonConstants.VALUE)
    :ivar type: fields.StringField(name=HightonConstants.TYPE)
    :ivar subject_field_id: fields.StringField(name=HightonConstants.SUBJECT_FIELD_ID)
    :ivar subject_field_label: fields.StringField(name=HightonConstants.SUBJECT_FIELD_LABEL)
    """
    TAG_NAME = HightonConstants.SUBJECT_DATA

    def __init__(self, **kwargs):
        self.value = fields.StringField(name=HightonConstants.VALUE)
        self.type = fields.StringField(name=HightonConstants.TYPE)
        self.subject_field_id = fields.StringField(name=HightonConstants.SUBJECT_FIELD_ID)
        self.subject_field_label = fields.StringField(name=HightonConstants.SUBJECT_FIELD_LABEL)

        super().__init__(**kwargs)
