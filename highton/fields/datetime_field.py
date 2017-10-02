import datetime
from xml.etree import ElementTree

from highton.fields.field import Field
from highton.fields.field_constants import FieldConstants


class DatetimeField(Field):
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def encode(self):
        """

        :return: the encoded element
        :rtype: xml.etree.ElementTree.Element
        """
        element = ElementTree.Element(
            self.name,
            attrib={
                'type': FieldConstants.DATETIME
            },
        )
        element = self._set_nil(element, lambda value: value.strftime(self.DATETIME_FORMAT))
        return element

    def decode(self, element):
        """

        :param element: the element which needs to be parsed
        :type element: xml.etree.ElementTree.Element
        :return: the parsed datetime object
        :rtype: datetime.datetime
        """
        if element.text:
            return datetime.datetime.strptime(element.text, self.DATETIME_FORMAT)
        else:
            return None
