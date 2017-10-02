from highton.highton_constants import HightonConstants
from highton.models.type_category import TypeCategory
from highton import call_mixins


class TaskCategory(
    TypeCategory,
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
    ENDPOINT = HightonConstants.TASK_CATEGORIES
    TAG_NAME = HightonConstants.TASK_CATEGORY
