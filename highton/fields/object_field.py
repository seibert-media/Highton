from xml.etree import ElementTree

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
        element = ElementTree.Element(self.name)
        element.append(self.value.encode())
        return element

    def decode(self, element):
        return self.init_class.decode(element)