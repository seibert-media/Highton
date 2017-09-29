from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields

class EmailAddress(
    HightonModel,
):
    TAG_NAME = HightonConstants.EMAIL_ADDRESS

    def __init__(self, **kwargs):
        self.location = fields.StringField(name=HightonConstants.LOCATION)
        self.address = fields.StringField(name=HightonConstants.ADDRESS)

        super().__init__(**kwargs)
