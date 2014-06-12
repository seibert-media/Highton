from person import Person
from company import Company


class Case(object):
    """
        Use:
        highrise_id,
        author_id,
        closed_at,
        created_at,
        updated_at,
        name,
        visible_to,
        group_id,
        owner_id,
        parties
    """
    def __init__(self):
        self.parties = []

    def save_data(self, case):
        self.highrise_id = case['id']

        for attr in [
            'author-id',
            'closed-at',
            'created-at',
            'updated-at',
            'name',
            'visible-to',
            'group-id',
            'owner-id',
        ]:
            setattr(self, attr.replace('-', '_'), case[attr])

    def set_parties(self, parties):
        for party in parties.getchildren():
            pass
