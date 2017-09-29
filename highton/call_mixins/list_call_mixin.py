from highton.call_mixins import Call
from highton import fields

class ListCallMixin(Call):
    @classmethod
    def list(cls, params=None):
        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.from_string(cls._get_request(params=params).text)
        )
