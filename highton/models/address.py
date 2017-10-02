from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class Address(
    HightonModel,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar location: fields.StringField(name=HightonConstants.LOCATION)
    :ivar city: fields.StringField(name=HightonConstants.CITY)
    :ivar country: fields.StringField(name=HightonConstants.COUNTRY)
    :ivar state: fields.StringField(name=HightonConstants.STATE)
    :ivar street: fields.StringField(name=HightonConstants.STREET)
    :ivar zip: fields.StringField(name=HightonConstants.ZIP)
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
