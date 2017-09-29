from xml.etree import ElementTree

from fields import Field


class ObjectField(Field):
    def __init__(self, name, init_class):
        super().__init__(name)
        self.init_class = init_class

    def encode(self):
        """
        Just encode the object you have as value
        
        :return: ElementTree.Element
        """
        element = ElementTree.Element(self.name)
        element.append(self.value.encode())
        return element

    def decode(self, element):
        return self.init_class.decode(element)
