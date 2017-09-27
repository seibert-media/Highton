from fields.field import Field
from xml.etree import ElementTree
from fields.field_constants import FieldConstants


class IntegerField(Field):
    def encode(self):
        return ElementTree.Element(
            tag=self.name,
            text=int(self.value),
            attrib={'type': FieldConstants.INTEGER},
        )

    def decode(self, element):
        return int(element.text)

