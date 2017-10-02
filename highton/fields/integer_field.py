from xml.etree import ElementTree

from highton.fields.field import Field
from highton.fields.field_constants import FieldConstants


class IntegerField(Field):
    def encode(self):
        """

        :return:
        :rtype: xml.etree.ElementTree.Element
        """
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.INTEGER},
        )
        element = self._set_nil(element, lambda value: str(value))
        return element

    def decode(self, element):
        """

        :param element:
        :type element: xml.etree.ElementTree.Element
        :return: the parsed int object
        :rtype: int
        """
        text = element.text
        if text:
            return int(text)
        else:
            return None

