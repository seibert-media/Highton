from abc import ABCMeta
from xml.etree import ElementTree


class Field(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.value = None

    def encode(self):
        element = ElementTree.Element(self.name)
        element.text = str(self.value)
        return element

    def decode(self, element):
        return element.text
