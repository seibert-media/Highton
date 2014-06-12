# -*- coding: utf-8 -*-
from custom_field import SubjectData
from tag import Tag


class Person(object):
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

    def __init__(self):
        for attr in [
            'phone_numbers',
            'email_addresses',
            'subject_datas',
            'tags',
        ]:
            setattr(self, attr, [])

    def set_phone_numbers(self, phone_numbers):
        for phone_number in phone_numbers:
            self.phone_numbers.append(
                PhoneNumber(
                    phone_number['id'],
                    phone_number['number'],
                    phone_number['location'],
                )
            )

    def set_email_addresses(self, email_addresses):
        for email_address in email_addresses:
            self.email_addresses.append(
                EmailAddress(
                    email_address['id'],
                    email_address['address'],
                    email_address['location'],
                )
            )

    def set_subject_datas(self, subject_datas):
        for subject_data in subject_datas:
            self.subject_datas.append(
                SubjectData(
                    subject_data['id'],
                    subject_data['value'],
                    subject_data['subject_field_id'],
                    subject_data['subject_field_labek'],
                )
            )

    def set_tags(self, tags):
        for tag in tags.getchildren():
            self.tags.append(
                Tag(
                    tag['id'],
                    tag['name'],
                )
            )

    def __unicode__(self):
        return unicode(self.highrise_id)


class PhoneNumber(object):
    def __init__(self):
        self.highrise_id = None
        self.number = None
        self.location = None


class EmailAddress(object):
    def __init__(self):
        self.higrise_id = None
        self.address = None
        self.location = None