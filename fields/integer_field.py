from fields.field import Field
from xml.etree import ElementTree
from fields.field_constants import FieldConstants


class IntegerField(Field):
    def encode(self):
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.INTEGER},
        )
        element.text=str(self.value)
        return element

    def decode(self, element):
        return int(element.text)

