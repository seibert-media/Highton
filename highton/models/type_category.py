from highton import (
    fields,
    call_mixins,
)
from highton.highton_constants import HightonConstants
from highton.models import HightonModel


class TypeCategory(
    HightonModel,
    call_mixins.ListCallMixin,
    call_mixins.DetailCallMixin,
    call_mixins.CreateCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DeleteCallMixin,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    :ivar color: fields.StringField(name=HightonConstants.COLOR)
    :ivar account_id: fields.IntegerField(name=HightonConstants.ACCOUNT_ID)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar elements_count: fields.IntegerField(name=HightonConstants.ELEMENTS_COUNT)
    """
    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME, required=True)
        self.color = fields.StringField(name=HightonConstants.COLOR)
        self.account_id = fields.IntegerField(name=HightonConstants.ACCOUNT_ID)
        self.created_at = fields.DatetimeField(name=HightonConstants.CREATED_AT)
        self.updated_at = fields.DatetimeField(name=HightonConstants.UPDATED_AT)
        self.elements_count = fields.IntegerField(name=HightonConstants.ELEMENTS_COUNT)
        super().__init__(**kwargs)
