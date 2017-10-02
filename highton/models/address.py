from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class Address(
    HightonModel,
):
    """

    :ivar id: fields.IntegerField
    :ivar location: fields.StringField
    :ivar city: fields.StringField
    :ivar country: fields.StringField
    :ivar state: fields.StringField
    :ivar street: fields.StringField
    :ivar zip: fields.StringField
    """
    TAG_NAME = HightonConstants.ADDRESS

    def __init__(self, **kwargs):
        self.location = fields.StringField(name=HightonConstants.LOCATION)
        self.city = fields.StringField(name=HightonConstants.CITY)
        self.country = fields.StringField(name=HightonConstants.COUNTRY)
        self.state = fields.StringField(name=HightonConstants.STATE)
        self.street = fields.StringField(name=HightonConstants.STREET)
        self.zip = fields.StringField(name=HightonConstants.ZIP)

        super().__init__(**kwargs)
