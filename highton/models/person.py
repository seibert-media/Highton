from highton import fields, call_mixins
from highton.highton_constants import HightonConstants
from highton.models.contact import Contact


class Person(
    Contact,
    call_mixins.ListCallMixin,
):
    ENDPOINT = HightonConstants.PEOPLE
    TAG_NAME = HightonConstants.PERSON

    def __init__(self, **kwargs):
        self.company_id = fields.IntegerField(name=HightonConstants.COMPANY_ID)
        self.company_name = fields.StringField(name=HightonConstants.COMPANY_NAME)
        self.first_name = fields.StringField(name=HightonConstants.FIRST_NAME)
        self.last_name = fields.StringField(name=HightonConstants.LAST_NAME)
        self.title = fields.StringField(name=HightonConstants.TITLE)

        super().__init__(**kwargs)
