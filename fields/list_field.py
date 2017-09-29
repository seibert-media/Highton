from xml.etree import ElementTree

from fields import Field
from fields.field_constants import FieldConstants


class ListField(Field):
    def __init__(self, name, init_class):
        super().__init__(name)
        self.init_class = init_class

    def encode(self):
        """
        Just iterate over the child elements and append them to the current element

        :return: ElementTree.Element
        """
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.ARRAY},
        )
        for item in self.value:
            element.append(item.encode())
        return element

    def decode(self, element):
        child_elements = []
        for child in element:
            child_elements.append(self.init_class.decode(child))
        return child_elements




