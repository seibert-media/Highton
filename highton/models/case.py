from highton import call_mixins
from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class Case(
    HightonModel,
    call_mixins.CreateCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DetailCallMixin,
    call_mixins.ListCallMixin,
    call_mixins.DeleteCallMixin,
    call_mixins.ListNoteCallMixin,
    call_mixins.ListEmailCallMixin,
    call_mixins.ListTagCallMixin,
    call_mixins.CreateTagCallMixin,
    call_mixins.DeleteTagCallMixin,
    call_mixins.ListTaskCallMixin,
    call_mixins.CreateNoteCallMixin,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar closed_at: fields.DatetimeField(name=HightonConstants.CLOSED_AT)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    :ivar visible_to: fields.StringField(name=HightonConstants.VISIBLE_TO)
    :ivar group_id: fields.IntegerField(name=HightonConstants.GROUP_ID)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    :ivar background: fields.StringField(name=HightonConstants.BACKGROUND)
    :ivar parties: fields.ListField(name=HightonConstants.PARTIES, init_class=Party)
    :ivar associated_parties: fields.ListField(name=HightonConstants.ASSOCIATED_PARTIES, init_class=AssociatedParty)
    """

    ENDPOINT = HightonConstants.CASES
    TAG_NAME = HightonConstants.CASE

    def __init__(self, **kwargs):
        from highton.models import (
            Party,
            AssociatedParty,
        )

        self.author_id = fields.IntegerField(name=HightonConstants.AUTHOR_ID)
        self.closed_at = fields.DatetimeField(name=HightonConstants.CLOSED_AT)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.name = fields.StringField(name=HightonConstants.NAME)
        self.visible_to = fields.StringField(name=HightonConstants.VISIBLE_TO)
        self.group_id = fields.IntegerField(name=HightonConstants.GROUP_ID)
        self.owner_id = fields.IntegerField(name=HightonConstants.OWNER_ID)
        self.background = fields.StringField(name=HightonConstants.BACKGROUND)
        self.parties = fields.ListField(name=HightonConstants.PARTIES, init_class=Party)
        self.associated_parties = fields.ListField(name=HightonConstants.ASSOCIATED_PARTIES, init_class=AssociatedParty)

        super().__init__(**kwargs)
