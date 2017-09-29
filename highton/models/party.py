from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields

class Party(
    HightonModel,
):
    ENDPOINT = HightonConstants.PARTIES
    TAG_NAME = HightonConstants.PARTY

    def __init__(self, **kwargs):
        from highton.models import Tag, ContactData, SubjectData

        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.background = fields.StringField(name=HightonConstants.BACKGROUND)
        self.company_id = fields.IntegerField(name=HightonConstants.COMPANY_ID)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.first_name = fields.StringField(name=HightonConstants.FIRST_NAME)
        self.name = fields.StringField(name=HightonConstants.NAME)
        self.group_id = fields.IntegerField(name=HightonConstants.GROUP_ID)
        self.last_name = fields.StringField(name=HightonConstants.LAST_NAME)
        self.owner_id = fields.IntegerField(name=HightonConstants.OWNER_ID)
        self.title = fields.StringField(name=HightonConstants.TITLE)
        self.type = fields.StringField(name=HightonConstants.TYPE)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.visible_to = fields.StringField(name=HightonConstants.VISIBLE_TO)
        self.company_name = fields.StringField(name=HightonConstants.COMPANY_NAME)
        self.linkedin_url = fields.StringField(name=HightonConstants.LINKEDIN_URL)
        self.avatar_url = fields.StringField(name=HightonConstants.AVATAR_URL)
        self.tags = fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
        self.contact_data = fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
        self.subject_datas = fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)

        super().__init__(**kwargs)
