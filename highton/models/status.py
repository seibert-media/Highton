from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class Status(
    HightonModel,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    """
    TAG_NAME = HightonConstants.STATUS

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME)
        super().__init__(**kwargs)
