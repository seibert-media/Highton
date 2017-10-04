from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import (
    fields,
    call_mixins,
)


class SubjectField(
    HightonModel,
    call_mixins.ListCallMixin,
    call_mixins.CreateCallMixin,
    call_mixins.UpdateCallMixin,
    call_mixins.DeleteCallMixin,
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar label: fields.StringField(name=HightonConstants.LABEL)
    :ivar type: fields.StringField(name=HightonConstants.TYPE)
    """
    TAG_NAME = HightonConstants.SUBJECT_FIELD
    ENDPOINT = HightonConstants.SUBJECT_FIELDS

    def __init__(self, **kwargs):
        self.label = fields.StringField(name=HightonConstants.LABEL)
        self.type = fields.StringField(name=HightonConstants.TYPE)

        super().__init__(**kwargs)

    @classmethod
    def list(cls, params=None):
        """
        Returns all subject fields
        params should have a type field with (party, deal)

        :param params:
        :type params: dict
        :return:
        :rtype:
        """
        return super().list(params)
