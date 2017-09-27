from abc import ABCMeta
from xml.etree import ElementTree


class Field(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.value = None

    def encode(self):
        return ElementTree.Element(tag=self.name, text=self.value)

    def decode(self, element):
        return element.text
