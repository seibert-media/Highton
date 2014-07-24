from .custom_field import SubjectData
from .tag import Tag


class Contact(object):
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
        for email_address in email_addresses.getchildren():
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
                    subject_data['subject_field_label'],
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


class PhoneNumber(object):
    def __init__(
            self,
            highrise_id,
            number,
            location,
    ):
        self.highrise_id = highrise_id.pyval
        self.number = number.pyval
        self.location = location.pyval


class EmailAddress(object):
    def __init__(
        self,
        highrise_id,
        address,
        location,
    ):
        self.highrise_id = highrise_id.pyval
        self.address = address.pyval
        self.location = location.pyval


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
        self.highrise_id = highrise_id.pyval
        self.city = city.pyval
        self.country = country.pyval
        self.location = location.pyval
        self.state = state.pyval
        self.street = street.pyval
