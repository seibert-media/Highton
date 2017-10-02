from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class WebAddress(
    HightonModel,
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar location: fields.StringField(name=HightonConstants.LOCATION)
    :ivar url: fields.StringField(name=HightonConstants.URL)
    """
    TAG_NAME = HightonConstants.WEB_ADDRESS

    def __init__(self, **kwargs):
        self.location = fields.StringField(name=HightonConstants.LOCATION)
        self.url = fields.StringField(name=HightonConstants.URL)

        super().__init__(**kwargs)
