from abc import ABCMeta

from highton import fields
from highton.highton_constants import HightonConstants
from highton.parsing.xml_decoder import XMLDecoder
from highton.parsing.xml_encoder import XMLEncoder


class HightonModel(XMLDecoder, XMLEncoder, metaclass=ABCMeta):
    """
    This class inherit from XMLDecoder and XMLEncoder which allows every HightonModel to be encoded and decoded in xml.

    :ivar id: fields.IntegerField(name=HightonConstants.ID)

    """
    ENDPOINT = None

    def __init__(self, **kwargs):
        self.id = fields.IntegerField(name=HightonConstants.ID)

        for key, value in kwargs.items():
            setattr(self, key, value)


