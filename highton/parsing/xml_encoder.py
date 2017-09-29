from abc import ABCMeta
from xml.etree import ElementTree

from highton import fields


class XMLEncoder(metaclass=ABCMeta):

    TAG_NAME = None

    def __setattr__(self, key, value):
        if key in self.__dict__ and isinstance(self.__dict__[key], fields.Field):
            self.__dict__[key].value = value
        else:
            object.__setattr__(self, key, value)

    @staticmethod
    def to_string(element):
        return ElementTree.tostring(element)

    def encode(self):
        root_element = ElementTree.Element(self.TAG_NAME)
        for value in [value for value in self.__dict__.values() if isinstance(value, fields.Field)]:
            root_element.append(value.encode())
        return root_element
