from highton import fields
from highton.highton_constants import HightonConstants
from highton.models import HightonModel


class Category(
    HightonModel,
):
    TAG_NAME = HightonConstants.CATEGORY

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.FIRST_NAME)

        super().__init__(**kwargs)
