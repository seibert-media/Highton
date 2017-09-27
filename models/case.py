from calls import ListCall
from models import HightonModel


class Case(
    HightonModel,
    ListCall,
):
    ENDPOINT = 'kases'
    TAG_NAME = 'kase'

