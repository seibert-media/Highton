from highton import call_mixins
from highton import fields
from highton.highton_constants import HightonConstants
from highton.models import HightonModel


class Attachment(
    HightonModel,
    call_mixins.Call
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar url: fields.StringField(name=HightonConstants.URL)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    :ivar size: fields.IntegerField(name=HightonConstants.SIZE)

    """
    TAG_NAME = HightonConstants.ATTACHMENT

    def __init__(self, **kwargs):
        self.url = fields.StringField(name=HightonConstants.URL)
        self.name = fields.StringField(name=HightonConstants.NAME)
        self.size = fields.IntegerField(name=HightonConstants.SIZE)

        super().__init__(**kwargs)

    def get(self):
        return self._get_request(endpoint='files/{}'.format(self.id), endpoint_suffix='').content
