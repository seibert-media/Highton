from xml.etree import ElementTree

from highton.fields import Field
from highton.fields.field_constants import FieldConstants


class ListField(Field):
    """
    The ListField parses the init_class objects in a list

    :ivar init_class: a Highton model
    """

    def __init__(self, name, init_class):
        super().__init__(name)
        self.init_class = init_class

    def encode(self):
        """
        Just iterate over the child elements and append them to the current element

        :return: the encoded element
        :rtype: xml.etree.ElementTree.Element
        """
        element = ElementTree.Element(
            self.name,
            attrib={'type': FieldConstants.ARRAY},
        )
        for item in self.value:
            element.append(item.encode())
        return element

    def decode(self, element):
        """

        :param element:
        :type element:
        :return: the parsed list with init_class objects
        :rtype: list
        """
        child_elements = []
        for child in element:
            child_elements.append(self.init_class.decode(child))
        return child_elements

    def to_serializable_value(self):
        """
        Run through the values and parse them to a serializable value

        :return:
        :rtype: list
        """
        return [child.to_serializable_value() for child in (self.value if self.value else [])]
