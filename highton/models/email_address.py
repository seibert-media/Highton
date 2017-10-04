from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class EmailAddress(
    HightonModel,
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar location: fields.StringField(name=HightonConstants.LOCATION)
    :ivar address: fields.StringField(name=HightonConstants.ADDRESS)
    """
    TAG_NAME = HightonConstants.EMAIL_ADDRESS

    def __init__(self, **kwargs):
        self.location = fields.StringField(name=HightonConstants.LOCATION, required=True)
        self.address = fields.StringField(name=HightonConstants.ADDRESS, required=True)

        super().__init__(**kwargs)
