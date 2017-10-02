from abc import ABCMeta
from xml.etree import ElementTree

from highton import fields


class FieldDoesNotExist(Exception):
    def __init__(self, obj, element):
        self.obj = obj
        self.element = element

    def __str__(self):
        return 'The field "{tag}" does not exist in {object}'.format(tag=self.element.tag, object=self.obj)


class XMLDecoder(metaclass=ABCMeta):
    """
    This class is an abstract class which helps to decode a XML String to the actual object which inherits from it

    """

    def __getattribute__(self, name):
        attribute_value = object.__getattribute__(self, name)
        if isinstance(attribute_value, fields.Field):
            return attribute_value.value
        return attribute_value

    def _get_field_names_to_attributes(self):

        return {
            value.name: key
            for key, value in self.__dict__.items()
            if isinstance(value, fields.Field)
        }

    def _get_field(self, attribute_name):
        return self.__dict__[attribute_name]

    @staticmethod
    def _set_field(xml_decoder_object, field_names_to_attributes, child_element):
        try:
            field = xml_decoder_object._get_field(
                field_names_to_attributes[child_element.tag]
            )
            field.value = field.decode(child_element)
        except KeyError:
            raise FieldDoesNotExist(xml_decoder_object, child_element)

    @staticmethod
    def element_from_string(string):
        """
        Make a Element from a str

        :param string: string you want to parse
        :type string: str
        :return: the parsed xml string
        :rtype: xml.etree.ElementTree.Element
        """
        return ElementTree.fromstring(string)

    @classmethod
    def decode(cls, root_element):
        """
        Decode the object to the object

        :param root_element: the parsed xml Element
        :type root_element: xml.etree.ElementTree.Element
        :return: the decoded Element as object
        :rtype: object
        """
        new_object = cls()
        field_names_to_attributes = new_object._get_field_names_to_attributes()
        for child_element in root_element:
            new_object._set_field(new_object, field_names_to_attributes, child_element)
        return new_object
