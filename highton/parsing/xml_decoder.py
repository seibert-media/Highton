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
    def __getattribute__(self, name):
        attribute_value = object.__getattribute__(self, name)
        if isinstance(attribute_value, fields.Field):
            return attribute_value.value
        return attribute_value

    def get_field_names_to_attributes(self):

        return {
            value.name: key
            for key, value in self.__dict__.items()
            if isinstance(value, fields.Field)
        }

    def get_field(self, attribute_name):
        return self.__dict__[attribute_name]

    @staticmethod
    def _set_field(xml_decoder_object, field_names_to_attributes, child_element):
        try:
            field = xml_decoder_object.get_field(
                field_names_to_attributes[child_element.tag]
            )
            field.value = field.decode(child_element)
        except KeyError:
            raise FieldDoesNotExist(xml_decoder_object, child_element)

    @staticmethod
    def from_string(string):
        return ElementTree.fromstring(string)

    @classmethod
    def decode(cls, root_element):
        new_object = cls()
        field_names_to_attributes = new_object.get_field_names_to_attributes()
        for child_element in root_element:
            new_object._set_field(new_object, field_names_to_attributes, child_element)
        return new_object
