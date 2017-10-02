from abc import ABCMeta
from xml.etree import ElementTree

from highton import fields


class XMLEncoder(metaclass=ABCMeta):

    """
    Encodes the object to an xml.etree.ElementTree.Element

    """

    TAG_NAME = None

    def __setattr__(self, key, value):
        if key in self.__dict__ and isinstance(self.__dict__[key], fields.Field):
            self.__dict__[key].value = value
        else:
            object.__setattr__(self, key, value)

    @staticmethod
    def element_to_string(element):
        """
        Parses the xml.etree.ElementTree.Element to a string

        :param element: a xml element
        :type element: xml.etree.ElementTree.Element
        :return: the parsed string
        :rtype: str
        """
        return ElementTree.tostring(element)

    def encode(self):
        """
        Encodes the object to a xml.etree.ElementTree.Element

        :return: the encoded element
        :rtype: xml.etree.ElementTree.Element
        """
        root_element = ElementTree.Element(self.TAG_NAME)
        for value in [value for value in self.__dict__.values() if isinstance(value, fields.Field)]:
            if value.required or value.value:
                root_element.append(value.encode())
        return root_element
