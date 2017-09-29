import datetime
from xml.etree import ElementTree

from highton.fields.field import Field
from highton.fields.field_constants import FieldConstants


class DateField(Field):
    DATE_FORMAT = '%Y-%m-%d'

    def encode(self):
        element =  ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.DATE},
        )
        element.text=self.value.isoformat()
        return element

    def decode(self, element):
        text = element.text
        if text:
            return datetime.datetime.strptime(text, self.DATE_FORMAT).date()
        else:
            return None
