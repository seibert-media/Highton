from abc import ABCMeta
from xml.etree import ElementTree


class Field(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.value = None

    def encode(self):
        element = ElementTree.Element(self.name)
        element = self._set_nil(element, lambda value: str(value))
        return element

    def decode(self, element):
        return element.text

    def _set_nil(self, element, value_parser):
        if self.value:
            element.text = value_parser(self.value)
        else:
            element.attrib['nil'] = 'true'
        return element