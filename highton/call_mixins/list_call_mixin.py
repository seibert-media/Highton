from highton.call_mixins import Call
from highton import fields


class ListCallMixin(Call):
    """
    A mixin to retrieve a list of a highrise endpoint

    """

    @classmethod
    def list(cls, params=None):
        """
        Retrieves a list of the model

        :param params: params as dictionary
        :type params: dict
        :return: the list of the parsed xml objects
        :rtype: list
        """
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(cls._get_request(params=params).text)
        )
