from xml.etree import ElementTree

from highton.fields.field import Field
from highton.fields.field_constants import FieldConstants


class IntegerField(Field):
    def encode(self):
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.INTEGER},
        )
        element = self._set_nil(element, lambda value: str(value))
        return element

    def decode(self, element):
        text = element.text
        if text:
            return int(text)
        else:
            return None

