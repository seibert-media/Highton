from highton import (
    fields,
    call_mixins,
)
from highton.highton_constants import HightonConstants
from highton.models import HightonModel


class Deal(
    HightonModel,
    call_mixins.ListCallMixin,
):
    """
    A deal which represents:

    https://github.com/basecamp/highrise-api/blob/master/sections/deals.md

    :ivar id: fields.IntegerField
    :ivar authod_id: fields.IntegerField
    :ivar account_id: fields.IntegerField
    :ivar background: fields.StringField
    :ivar category_id: fields.IntegerField
    :ivar created_at: fields.DatetimeField
    :ivar currency: fields.StringField
    :ivar duration: fields.IntegerField
    :ivar group_id: fields.IntegerField
    :ivar name: fields.StringField
    :ivar owner_id: fields.IntegerField
    :ivar party_id: fields.IntegerField
    :ivar price: fields.IntegerField
    :ivar price_type: fields.StringField
    :ivar responsible_party_id: fields.IntegerField
    :ivar status: fields.StringField
    :ivar status_changed_on: fields.DateField
    :ivar updated_at: fields.DatetimeField
    :ivar visible_to: fields.StringField
    :ivar party: fields.ObjectField
    :ivar category: fields.ObjectField
    :ivar tags: fields.ListField
    :ivar parties: fields.ListField
    :ivar contact_data: fields.ObjectField
    :ivar subject_datas: fields.ListField
    :ivar associated_parties: fields.ListField
    """

    ENDPOINT = HightonConstants.DEALS
    TAG_NAME = HightonConstants.DEAL

    def __init__(self, **kwargs):
        """
        Init a deal with the attributes

        :param kwargs:
        :type kwargs:
        """
        from highton.models import (
            Tag,
            ContactData,
            SubjectData,
            Party,
            AssociatedParty,
            Category,
        )

        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.account_id = fields.IntegerField(name=HightonConstants.ACCOUNT_ID)
        self.background = fields.StringField(name=HightonConstants.BACKGROUND)
        self.category_id = fields.IntegerField(name=HightonConstants.CATEGORY_ID)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.currency = fields.StringField(name=HightonConstants.CURRENCY)
        self.duration = fields.IntegerField(name=HightonConstants.DURATION)
        self.group_id = fields.IntegerField(name=HightonConstants.GROUP_ID)
        self.name = fields.StringField(name=HightonConstants.NAME)
        self.owner_id = fields.IntegerField(name=HightonConstants.OWNER_ID)
        self.party_id = fields.IntegerField(name=HightonConstants.PARTY_ID)
        self.price = fields.IntegerField(name=HightonConstants.PRICE)
        self.price_type = fields.StringField(name=HightonConstants.PRICE_TYPE)
        self.responsible_party_id = fields.IntegerField(name=HightonConstants.RESPONSIBLE_PARTY_ID)
        self.status = fields.StringField(name=HightonConstants.STATUS)
        self.status_changed_on = fields.DateField(name=HightonConstants.STATUS_CHANGED_ON)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.visible_to = fields.StringField(name=HightonConstants.VISIBLE_TO)
        self.party = fields.ObjectField(name=HightonConstants.PARTY, init_class=Party)
        self.category = fields.ObjectField(name=HightonConstants.CATEGORY, init_class=Category)

        self.tags = fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
        self.parties = fields.ListField(name=HightonConstants.PARTIES, init_class=Party)
        self.contact_data = fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
        self.subject_datas = fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)
        self.associated_parties = fields.ListField(name=HightonConstants.ASSOCIATED_PARTIES, init_class=AssociatedParty)

        super().__init__(**kwargs)
