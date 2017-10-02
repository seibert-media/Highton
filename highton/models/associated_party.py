from highton.models import Party
from highton.highton_constants import HightonConstants


class AssociatedParty(
    Party,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar background: fields.StringField(name=HightonConstants.BACKGROUND)
    :ivar company_id: fields.IntegerField(name=HightonConstants.COMPANY_ID)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar first_name: fields.StringField(name=HightonConstants.FIRST_NAME)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    :ivar group_id: fields.IntegerField(name=HightonConstants.GROUP_ID)
    :ivar last_name: fields.StringField(name=HightonConstants.LAST_NAME)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    :ivar title: fields.StringField(name=HightonConstants.TITLE)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar visible_to: fields.StringField(name=HightonConstants.VISIBLE_TO)
    :ivar company_name: fields.StringField(name=HightonConstants.COMPANY_NAME)
    :ivar linkedin_url: fields.StringField(name=HightonConstants.LINKEDIN_URL)
    :ivar avatar_url: fields.StringField(name=HightonConstants.AVATAR_URL)
    :ivar type: fields.StringField(name=HightonConstants.TYPE)
    :ivar tags: fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
    :ivar contact_data: fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
    :ivar subject_datas: fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)
    """
    TAG_NAME = HightonConstants.ASSOCIATED_PARTY
