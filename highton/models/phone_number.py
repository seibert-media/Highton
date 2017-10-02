from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class PhoneNumber(
    HightonModel,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar location: fields.StringField(name=HightonConstants.LOCATION)
    :ivar number: fields.StringField(name=HightonConstants.NUMBER)
    """
    TAG_NAME = HightonConstants.PHONE_NUMBER

    def __init__(self, **kwargs):
        self.location = fields.StringField(name=HightonConstants.LOCATION)
        self.number = fields.StringField(name=HightonConstants.NUMBER)

        super().__init__(**kwargs)
