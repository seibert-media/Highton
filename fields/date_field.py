import datetime

from fields.field import Field
from xml.etree import ElementTree
from fields.field_constants import FieldConstants


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
        return datetime.datetime.strptime(element.text, self.DATE_FORMAT).date()
