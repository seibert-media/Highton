from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class TwitterAccount(
    HightonModel,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar location: fields.StringField(name=HightonConstants.LOCATION)
    :ivar username: fields.StringField(name=HightonConstants.USERNAME)
    :ivar url: fields.StringField(name=HightonConstants.URL)
    """
    TAG_NAME = HightonConstants.TWITTER_ACCOUNT

    def __init__(self, **kwargs):
        self.location = fields.StringField(name=HightonConstants.LOCATION)
        self.username = fields.StringField(name=HightonConstants.USERNAME)
        self.url = fields.StringField(name=HightonConstants.URL)

        super().__init__(**kwargs)
