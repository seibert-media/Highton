from highton.fields import Field


class ObjectField(Field):
    """
    The ObjectFIeld parses the init_class object

    :ivar init_class: a Highton model
    """
    def __init__(self, name, init_class):
        super().__init__(name)
        self.init_class = init_class

    def encode(self):
        """
        Just encode the object you have as value
        
        :return: the parsed element
        :rtype: xml.etree.ElementTree.Element
        """
        return self.value.encode()

    def decode(self, element):
        return self.init_class.decode(element)

    def to_serializable_value(self):
        """
        Run through all fields of the object and parse the values

        :return:
        :rtype: dict
        """
        return {
            name: field.to_serializable_value()
            for name, field in self.value.__dict__.items()
            if isinstance(field, Field) and self.value
        }

