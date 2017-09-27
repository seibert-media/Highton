import datetime

from fields.field import Field
from xml.etree import ElementTree
from fields.field_constants import FieldConstants


class DatetimeField(Field):
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def encode(self):
        return ElementTree.Element(
            tag=self.name,
            text=self.value.strftime(self.DATETIME_FORMAT),
            attrib={'type': FieldConstants.DATETIME},
        )

    def decode(self, element):
        return datetime.datetime.strptime(element.text, self.DATETIME_FORMAT)

