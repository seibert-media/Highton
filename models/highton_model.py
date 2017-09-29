from abc import ABCMeta

import fields
from highton_constants import HightonConstants
from parsing.xml_decoder import XMLDecoder
from parsing.xml_encoder import XMLEncoder


class HightonModel(XMLDecoder, XMLEncoder, metaclass=ABCMeta):
    ENDPOINT = None
    TAG_NAME = None

    def __init__(self, **kwargs):
        self.id = fields.IntegerField(name=HightonConstants.ID)

        for key, value in kwargs.items():
            setattr(self, key, value)

