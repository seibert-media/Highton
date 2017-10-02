from highton import fields
from highton.models import HightonModel
from highton.highton_constants import HightonConstants


class Contact(
    HightonModel,

):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar background: fields.StringField(name=HightonConstants.BACKGROUND)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar group_id: fields.IntegerField(name=HightonConstants.GROUP_ID)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar visible_to: fields.StringField(name=HightonConstants.VISIBLE_TO)
    :ivar linkedin_url: fields.StringField(name=HightonConstants.LINKEDIN_URL)
    :ivar avatar_url: fields.StringField(name=HightonConstants.AVATAR_URL)
    :ivar tags: fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
    :ivar contact_data: fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
    :ivar subject_datas: fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)
    """
    def __init__(self, **kwargs):
        from highton.models import (
            Tag,
            ContactData,
            SubjectData,
        )

        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.background = fields.StringField(name=HightonConstants.BACKGROUND)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.group_id = fields.IntegerField(name=HightonConstants.GROUP_ID)
        self.owner_id = fields.IntegerField(name=HightonConstants.OWNER_ID)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.visible_to = fields.StringField(name=HightonConstants.VISIBLE_TO)
        self.linkedin_url = fields.StringField(name=HightonConstants.LINKEDIN_URL)
        self.avatar_url = fields.StringField(name=HightonConstants.AVATAR_URL)
        self.tags = fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
        self.contact_data = fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
        self.subject_datas = fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)

        super().__init__(**kwargs)
