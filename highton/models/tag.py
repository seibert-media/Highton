from highton import call_mixins
from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class Tag(
    HightonModel,
    call_mixins.ListCallMixin,
):
    ENDPOINT = HightonConstants.TAGS
    TAG_NAME = HightonConstants.TAG

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME)

        super().__init__(**kwargs)
