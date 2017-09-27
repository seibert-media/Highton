from calls import Call


class ListCall(Call):
    @classmethod
    def list(cls, *args, **kwargs):
        return cls.decode(cls._get_request(cls.ENDPOINT + '.xml', *args, **kwargs))
