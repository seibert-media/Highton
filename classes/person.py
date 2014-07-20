# -*- coding: utf-8 -*-
from .contact import Contact

from .tools import to_datetime


class Person(Contact):
    """
        Feel free to work with this attributes.
        highrise_id,
        first_name,
        last_name,
        title,
        background,
        linkedin_url,
        avatar_url,
        company_id,
        company_name,
        created_at,
        updated_at,
        visible_to,
        owner_id,
        group_id,
        author_id,
        phone_numbers,
        email_addresses,
        subject_datas,
        tags
    """
    def save_data(self, person):
        self.highrise_id = person['id'].pyval
        self.created_at = to_datetime(person['created-at'].pyval)
        self.updated_at = to_datetime(person['updated-at'].pyval)
        for attr in [
            'first-name',
            'last-name',
            'title',
            'background',
            'linkedin-url',
            'avatar-url',
            'company-id',
            'company-name',
            'visible-to',
            'owner-id',
            'group-id',
            'author-id',
        ]:
            setattr(self, attr.replace('-', '_'), person[attr].pyval)

        for attr in [
            'phone-numbers',
            'email-addresses',
            'addresses',
        ]:
            if hasattr(person['contact-data'], attr):
                getattr(self, 'set_' + attr.replace('-', '_'))(
                    person['contact-data'][attr])

        for attr in [
            'subject_datas',
            'tags',
        ]:
            if hasattr(person, attr):
                getattr(self, 'set_' + attr.replace('-', '_'))(person[attr])
