import datetime
from xml.etree import ElementTree

from highton.fields.field import Field
from highton.fields.field_constants import FieldConstants


class BooleanField(Field):
    """
    The BooleanField represents a field which value will be parsed to Highrise specific boolean format

    """

    TRUE = 'true'
    FALSE = 'false'

    MAPPING = {
        True: TRUE,
        False: FALSE,
    }

    def encode(self):
        """

        :return:
        :rtype: xml.etree.ElementTree.Element
        """
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.BOOLEAN},
        )
        element.text = self.MAPPING[self.value]
        return element

    def decode(self, element):
        """

        :param element: the element which needs to be parsed
        :type element: xml.etree.ElementTree.Element
        :return: datetime.date
        :rtype: the parsed date object
        """
        return element.text == self.TRUE
