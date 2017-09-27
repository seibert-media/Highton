from abc import ABCMeta
from xml.etree import ElementTree
import inspect

import fields


class FieldDoesNotExist(Exception):
    def __init__(self, element):
        self.element = element

    def __str__(self):
        return 'The field "{tag}" does not exist'.format(tag=self.element.tag)


class XMLDecoder(metaclass=ABCMeta):
    def __getattribute__(self, name):
        attribute_value = object.__getattribute__(self, name)
        if isinstance(attribute_value, fields.Field):
            return attribute_value.value
        return attribute_value

    @classmethod
    def get_field_names_to_attributes(cls):

        return {
            value.name: key
            for key, value in inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
            if isinstance(value, fields.Field)
        }

    @classmethod
    def get_field(cls, attribute_name):
        return dict(inspect.getmembers(cls, lambda a: not (inspect.isroutine(a))))[attribute_name]

    @staticmethod
    def _set_field(xml_decoder_object, field_names_to_attributes, child_element):
        try:
            field = xml_decoder_object.get_field(
                field_names_to_attributes[child_element.tag]
            )
            field.value = field.decode(child_element)
        except KeyError:
            raise FieldDoesNotExist(child_element)

    @classmethod
    def decode(cls, xml_string):
        root = ElementTree.fromstring(xml_string)
        new_object = cls()
        field_names_to_attributes = cls.get_field_names_to_attributes()
        for child_element in root:
            cls._set_field(new_object, field_names_to_attributes, child_element)
        return new_object
