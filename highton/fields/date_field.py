import datetime
from xml.etree import ElementTree

from highton.fields.field import Field
from highton.fields.field_constants import FieldConstants


class DateField(Field):
    """
    The DateField represents a field which value will be parsed to Highrise specific date format

    """
    DATE_FORMAT = '%Y-%m-%d'

    def encode(self):
        """

        :return:
        :rtype: xml.etree.ElementTree.Element
        """
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.DATE},
        )
        element = self._set_nil(element, lambda value: value.isoformat())
        return element

    def decode(self, element):
        """

        :param element: the element which needs to be parsed
        :type element: xml.etree.ElementTree.Element
        :return: datetime.date
        :rtype: the parsed date object
        """
        text = element.text
        if text:
            return datetime.datetime.strptime(text, self.DATE_FORMAT).date()
        else:
            return None
