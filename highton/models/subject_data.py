from highton import call_mixins
from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class SubjectData(
    HightonModel,
    call_mixins.ListCallMixin,
):
    ENDPOINT = HightonConstants.CASES
    TAG_NAME = HightonConstants.CASE

    def __init__(self, **kwargs):
        self.value = fields.StringField(name=HightonConstants.VALUE)
        self.type = fields.StringField(name=HightonConstants.TYPE)
        self.subject_field_id = fields.StringField(name=HightonConstants.SUBJECT_FIELD_ID)
        self.subject_field_label = fields.StringField(name=HightonConstants.SUBJECT_FIELD_LABEL)

        super().__init__(**kwargs)
