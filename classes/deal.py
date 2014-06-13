from person import Person
from company import Company
from category import Category


class Deal(object):
    """
        Use:
        account_id
        author_id
        background
        category_id
        created_at
        currency
        duration
        group_id
        id
        name
        owner_id
        party_id
        price
        price_type
        responsible_party_id
        status
        status_changed_on
        updated_at
        visible_to
        category
        party
        parties
    """

    def __init__(self):
        self.parties = []

    def save_data(self, deal):
        self.highrise_id = deal['id']

        for attr in [
            'account-id',
            'author-id',
            'background',
            'category-id',
            'created-at',
            'currency',
            'duration',
            'group-id',
            'name',
            'owner-id',
            'party-id',
            'price',
            'price-type',
            'responsible-party-id',
            'status',
            'status-changed-on',
            'updated-at',
            'visible-to',
        ]:
            setattr(self, attr.replace('-', '_'), deal[attr])

        if hasattr(deal, 'category'):
            category = Category()
            category.save_data(deal['category'])
            self.category = category

        if hasattr(deal, 'party'):
            if deal['party']['type'] == 'Person':
                person = Person()
                person.save_data(deal['party'])
                self.party = person
            elif deal['party']['type'] == 'Company':
                company = Company()
                company.save_data(deal['party'])
                self.party = company


        if hasattr(deal, 'parties'):
            self.set_parties(deal['parties'])

    def set_parties(self, parties):
        for party in parties.getchildren():
            if party['type'] == 'Person':
                person = Person()
                person.save_data(party)
                self.parties.append(person)
            elif party['type'] == 'Company':
                company = Company()
                company.save_data(party)
                self.parties.append(company)
