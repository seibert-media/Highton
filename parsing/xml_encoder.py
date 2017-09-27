from abc import ABCMeta


class XMLEncoder(metaclass=ABCMeta):
    def __setattr__(self, key, value):
        if key in self.__dict__ and isinstance(self.__dict__[key], fields.Field):
            self.__dict__[key].value = value
        else:
            object.__setattr__(self, key, value)

    def encode(self):
        pass
