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
            'addresses'
        ]:
            setattr(self, attr, [])

    def set_addresses(self, addresses):
        for address in addresses.getchildren():
            self.addresses.append(
                Address(
                    address['id'],
                    address['city'],
                    address['country'],
                    address['location'],
                    address['state'],
                    address['street'],
                )
            )

    def set_phone_numbers(self, phone_numbers):
        for phone_number in phone_numbers.getchildren():
            self.phone_numbers.append(
                PhoneNumber(
                    phone_number['id'],
                    phone_number['number'],
                    phone_number['location'],
                )
            )

    def set_email_addresses(self, email_addresses):
        print 'rund'
        for email_address in email_addresses.getchildren():
            print email_address.__dict__
            self.email_addresses.append(
                EmailAddress(
                    email_address['id'],
                    email_address['address'],
                    email_address['location'],
                )
            )

    def set_subject_datas(self, subject_datas):
        for subject_data in subject_datas.getchildren():
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
    def __init__(
            self,
            highrise_id,
            number,
            location,
        ):
        self.highrise_id = highrise_id
        self.number = number
        self.location = location


class EmailAddress(object):
    def __init__(
        self,
        highrise_id,
        address,
        location,
    ):
        self.higrise_id = highrise_id
        self.address = address
        self.location = location


class Address(object):
    def __init__(
        self,
        highrise_id,
        city,
        country,
        location,
        state,
        street,
    ):
        self.highrise_id = highrise_id
        self.city = city
        self.country = country
        self.location = location
        self.state = state
        self.street = street