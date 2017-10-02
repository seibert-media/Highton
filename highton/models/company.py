from highton import (
    fields,
    call_mixins,
)
from highton.highton_constants import HightonConstants
from highton.models.contact import Contact


class Company(
    Contact,
    call_mixins.ListCallMixin,
):
    ENDPOINT = HightonConstants.COMPANIES
    TAG_NAME = HightonConstants.COMPANY

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME)

        super().__init__(**kwargs)
