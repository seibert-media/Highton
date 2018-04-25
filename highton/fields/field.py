from abc import ABCMeta
from xml.etree import ElementTree


class Field(metaclass=ABCMeta):
    """
    This is an abstract class for a field, which makes the base for an encode and decode method

    :ivar name: name of the field which needed to serialize this field to a xml object
    :ivar required: if the field is required when you create or update an object
    :ivar value: the value of the field
    """
    def __init__(self, name, required=False):
        self.name = name
        self.required = required
        self.value = None

    def encode(self):
        """
        Encodes the value of the field and put it in the element
        also make the check for nil=true if there is one

        :return: returns the encoded element
        :rtype: xml.etree.ElementTree.Element
        """
        element = ElementTree.Element(self.name)
        element = self._set_nil(element, lambda value: str(value))
        return element

    def decode(self, element):
        """
        Decodes the value of the element

        :param element:
        :type element:
        :return:
        :rtype:
        """
        return element.text

    def _set_nil(self, element, value_parser):
        """
        Method to set an attribute of the element.
        If the value of the field is None then set the nil='true' attribute in the element

        :param element: the element which needs to be modified
        :type element: xml.etree.ElementTree.Element
        :param value_parser: the lambda function which changes will be done to the self.value
        :type value_parser: def
        :return: the element with or without the specific attribute
        :rtype: xml.etree.ElementTree.Element
        """
        if self.value:
            element.text = value_parser(self.value)
        else:
            element.attrib['nil'] = 'true'
        return element

    def to_serializable_value(self):
        """
        Parse the value to a serializable pythonic value
        Default: Just return the value

        :return:
        :rtype: Any
        """
        return self.value
