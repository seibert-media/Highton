import datetime

from fields.field import Field
from xml.etree import ElementTree
from fields.field_constants import FieldConstants


class DateField(Field):
    DATE_FORMAT = '%Y-%m-%d'

    def encode(self):
        return ElementTree.Element(
            tag=self.name,
            text=self.value.isoformat(),
            attrib={'type': FieldConstants.DATE},
        )

    def decode(self, element):
        return datetime.datetime.strptime(element.text, self.DATE_FORMAT).date()
