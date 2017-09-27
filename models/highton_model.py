from abc import ABCMeta

import fields
from highton_constants import HightonConstants
from parsing.xml_decoder import XMLDecoder
from parsing.xml_encoder import XMLEncoder


class HightonModel(XMLDecoder, XMLEncoder):
    ENDPOINT = None
    TAG_NAME = None

    id = fields.IntegerField(name=HightonConstants.ID)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

