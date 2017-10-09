from highton import call_mixins
from highton import fields
from highton.highton_constants import HightonConstants
from highton.models import HightonModel


class Tag(
    HightonModel,
    call_mixins.ListCallMixin,
    call_mixins.DetailCallMixin,
    call_mixins.DeleteCallMixin,
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    """
    ENDPOINT = HightonConstants.TAGS
    TAG_NAME = HightonConstants.TAG

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME)

        super().__init__(**kwargs)

    @classmethod
    def get(cls, object_id):
        """
        Get all parties (people and companies) associated with a given tag.
        :param object_id: the primary id of the model
        :type object_id: integer
        :return: the parties
        :rtype: list
        """
        from highton.models.party import Party
        return fields.ListField(name=Party.ENDPOINT, init_class=Party).decode(
            cls.element_from_string(
                cls._get_request(endpoint=cls.ENDPOINT + '/' + str(object_id)).text
            )
        )
