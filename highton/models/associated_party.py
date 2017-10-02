from highton.models import Party
from highton.highton_constants import HightonConstants

class AssociatedParty(
    Party,
):
    TAG_NAME = HightonConstants.ASSOCIATED_PARTY

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

