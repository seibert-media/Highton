import logging

import requests
from lxml import objectify, etree
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Highton:
    GET_REQUEST = 'GET'
    POST_REQUEST = 'POST'
    PUT_REQUEST = 'PUT'
    DELETE_REQUEST = 'DELETE'
    HIGHRISE_URL = 'highrisehq.com'
    SUBJECT_TYPES = ['companies', 'kases', 'deals', 'people']

    class RequestException(Exception):
        """
        Offers an Exception in case of a request that timed-out, failed or was malformed.
        """
        pass

    class InsufficentParametersException(Exception):
        """
        Offers an Exception in case of a method call that did not receive the correct parameters.
        """
        pass

    def __init__(self, user, api_key):
        """
        :param user: Your personal username for the Highrise API
        :param api_key: Your personal API-Key for the Highrise API
        """
        self._user = user
        self._api_key = api_key

    """
    General methods
    """

    @staticmethod
    def _xml_to_object(xml):
        """
        Parses valid XML into Python ElementTree objects with the ability to parse them back into XML later on.

        :param xml: Valid XML as a string
        :return: A Python ElementTree object
        """
        return objectify.fromstring(xml)

    @staticmethod
    def _object_to_xml(element):
        """
        Parses a Python ElementTree object into valid XML.

        :param dictionary: A Python ElementTree object
        :return: Valid XML as a string
        """
        try:
            return str(etree.tostring(element))
        except:
            return {}

    @staticmethod
    def _check_for_parameters(subject_type, types):
        """
        Is used within many API methods to check if a correct 'subject_type' was selected.
        It raises an Exception otherwise.

        :param subject_type: The type to check against
        :param types: A list of types to check for
        """
        if subject_type not in types:
            raise Highton.InsufficentParametersException(f'The parameter subject must be in {types}')

    @staticmethod
    def _create_person(first_name, last_name=None, company_name=None, company_id=None, title=None, **kwargs):
        person = etree.Element('person')
        first = etree.SubElement(person, 'first-name')
        first.text = first_name
        last = etree.SubElement(person, 'last-name')
        last.text = last_name
        company = etree.SubElement(person, 'company-name')
        company.text = company_name
        companyid = etree.SubElement(person, 'company-id')
        companyid.text = str(company_id) if company_id else None
        person_title = etree.SubElement(person, 'title')
        person_title.text = title

        if kwargs:
            Highton._create_contact_data(person, **kwargs)

        return person

    @staticmethod
    def _create_contact_data(subject, email_addresses=None, phone_numbers=None, custom_fields=None,
                             web_addresses=None, addresses=None, tags=None):

        contact_data = etree.SubElement(subject, 'contact-data')
        emails = etree.SubElement(contact_data, 'email-addresses', type="array")
        if email_addresses:
            for email_address in email_addresses:
                email = etree.SubElement(emails, 'email-address')
                address = etree.SubElement(email, 'address')
                address.text = email_address.get('address')
                location = etree.SubElement(email, 'location')
                location.text = email_address.get('location')

        websites = etree.SubElement(contact_data, 'web-addresses', type="array")
        if web_addresses:
            for web_address in web_addresses:
                website = etree.SubElement(websites, 'web-address')
                url = etree.SubElement(website, 'url')
                url.text = web_address.get('url')
                location = etree.SubElement(website, 'location')
                location.text = web_address.get('location')

        addresses_data = etree.SubElement(contact_data, 'addresses', type="array")
        if addresses:
            for address in addresses:
                address_data = etree.SubElement(addresses_data, 'address')
                city = etree.SubElement(address_data, 'city')
                city.text = address.get('city')
                country = etree.SubElement(address_data, 'country')
                country.text = address.get('country')
                location = etree.SubElement(address_data, 'location')
                location.text = address.get('location')
                street = etree.SubElement(address_data, 'street')
                street.text = address.get('street')
                zip = etree.SubElement(address_data, 'zip')
                zip.text = address.get('zip')

        phones = etree.SubElement(contact_data, 'phone-numbers', type="array")
        if phone_numbers:
            for phone_number in phone_numbers:
                website = etree.SubElement(phones, 'phone-number')
                number = etree.SubElement(website, 'number')
                number.text = phone_number.get('number')
                location = etree.SubElement(website, 'location')
                location.text = phone_number.get('location')

        subject_datas = etree.SubElement(contact_data, 'subject_datas', type="array")
        if custom_fields:
            for custom_field in custom_fields:
                subject_data = etree.SubElement(subject_datas, 'subject_data', type="array")
                subject_field_id = etree.SubElement(subject_data, 'subject_field_id', type="integer")
                subject_field_id.text = custom_field.get('subject_field_id')
                value = etree.SubElement(subject_data, 'value')
                value.text = custom_field.get('value')

        tags_data = etree.SubElement(contact_data, 'tags')
        if tags:
            for tag in tags:
                tag_data = etree.SubElement(tags_data, 'tag')
                name = etree.SubElement(tag_data, 'name')
                name.text = tag.get('name')

        return contact_data

    @staticmethod
    def _create_company(name, background=None, **kwargs):
        company = etree.Element('company')
        company_name = etree.SubElement(company, 'name')
        company_name.text = name
        company_background = etree.SubElement(company, 'background')
        company_background.text = background

        if kwargs:
            Highton._create_contact_data(company, **kwargs)
        return company

    def _send_request(self, method, endpoint, params=None, data=None):
        """
        Creates and sends every request made with the API wrapper

        :param method: One of the HTTP methods from the constants within the class: (GET, POST, PUT, DELETE)
        :param endpoint: The endpoint of the API (without the file extension '.xml')
        :param params: Parameters to be URL-encoded and sent within the request
        :param data: HTTP body data to be sent within the request
        :return: The HTTP response from the API
        """
        response = requests.request(
            method=method,
            url=f'https://{self._user}.{Highton.HIGHRISE_URL}/{endpoint}.xml',
            headers={'Content-Type': 'application/xml'},
            auth=HTTPBasicAuth(username=self._api_key, password=''),
            params=params,
            data=data,
        )

        if not response.ok:
            raise Highton.RequestException(response.status_code)
        else:
            return response

    def _make_request(self, method, endpoint, params=None, data=None):
        """
        Calls the request method and also parses to and from XML. It catches Exceptions as well in case of an error.

        :param method: One of the HTTP methods from the constants within the class: (GET, POST, PUT, DELETE)
        :param endpoint: The endpoint of the API (without the file extension '.xml')
        :param params: Parameters to be URL-encoded and sent within the request
        :param data: HTTP body data to be sent within the request
        :return: The HTTP status code in case there was no content in the response else the content
        """
        try:
            response = self._send_request(
                method=method,
                endpoint=endpoint,
                params=params,
                data=self._object_to_xml(data)
            )

            if len(response.content) > 1:
                # return self._parse_from_xml_to_dict(response.content)
                return self._xml_to_object(response.content)
            else:
                return response.status_code
        except Highton.RequestException as e:
            logger.error(
                f'The {method}-request towards the endpoint "/{endpoint}.xml" failed with HTTP-Code {str(e)}'
            )

    """
    API methods
    """

    """
    Section: People
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/people.md
    """

    def get_people(self, since=None, page=0):
        """
        Retrieves all the people, optionally since a certain date.

        :param since: A native Python datetime object
        :param page: Each page per 500 entries
        :return: A list of dictionaries of people
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='people',
            params={
                'since': since.strftime('%Y%m%d%H%M%S') if since else None,
                'n': page * 500,
            },
        )

    def get_people_by_tag(self, tag_id):
        """
        Retrieves all the people tagged with a certain tag.

        :param tag_id: The ID of any tag
        :return: A list of dictionaries of people
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'people',
            params={
                'tag_id': tag_id,
            },
        )

    def search_people(self, term=None, page=0, **criteria):
        """
        Retrieves people by search terms and/or criteria.

        :param term: A search term
        :param page: Each page per 25 entries
        :param criteria: Keyword arguments with any criteria one uses in Highrise e.g. state, zip, city
        :return: A list of dictionaries of people
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='people/search',
            params={
                **{f'criteria[{k}]': v for k, v in criteria.items()},
                **{'n': page * 25},
                **{'term': term},
            }
        )

    def get_people_of_company(self, company):
        """
        Retrieves people that belong to a certain company

        :param company: The company as a dictionary preferrably returned from an earlier API call
        :return: A list of dictionaries of people
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'companies/{company["id"]["#text"]}/people',
        )

    def get_person(self, subject_id):
        """
        Retrieves a single person by ID.

        :param subject_id: The ID of the person in Highrise
        :return: A dictionary of the person
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'people/{subject_id}',
        )

    def create_person(self, first_name, **kwargs):
        """
        Creates a new person.

        :param person: A dictionary consisting of a person with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/people.md#create-person
        :return: If the API call was successful the just created person will be returned
        """
        person = self._create_person(first_name, **kwargs)

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint='people',
            data=person,
        )

    def update_person(self, person):
        """
        Updates a person.

        :param person: A dictionary consisting of a person with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/people.md#create-person
        :return: If the API call was successful the just updated person will be returned
        """
        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'people/{person.id}',
            data=person,
            params={'reload': 'true'}
        )

    def destroy_person(self, person):
        """
        Deletes a person.

        :param person: A dictionary consisting of a person with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/people.md#create-person
        :return: The HTTP status code of the response of the DELETE request
        """
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'people/{person.id}',
        )

    """
    Section: Companies
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/companies.md
    """

    def get_companies(self, since, page=0):
        """
        Retrieves all the companies, optionally since a certain date.

        :param since: A native Python datetime object
        :param page: Each page per 500 entries
        :return: A list of dictionaries of companies
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='companies',
            params={
                'since': since.strftime('%Y%m%d%H%M%S') if since else None,
                'n': page * 500,
            }
        )

    def get_companies_by_tag(self, tag_id):
        """
        Retrieves all the companies tagged with a certain tag.

        :param tag_id: The ID of any tag
        :return: A list of dictionaries of companies
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'companies',
            params={
                'tag_id': tag_id,
            }
        )

    def search_companies(self, term=None, page=0, **criteria):
        """
        Retrieves companies by search terms and/or criteria.

        :param term: A search term
        :param page: Each page per 25 entries
        :param criteria: Keyword arguments with any criteria one uses in Highrise e.g. state, zip, city
        :return: A list of dictionaries of companies
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='companies/search',
            params={
                **{f'criteria[{k}]': v for k, v in criteria.items()},
                **{'n': page * 25},
                **{'term': term},
            },
        )

    def get_company(self, subject_id):
        """
        Retrieves a single company by ID.

        :param subject_id: The ID of the company in Highrise
        :return: A dictionary of the company
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'companies/{subject_id}',
        )

    def create_company(self, name, **kwargs):
        """
        Creates a new person.

        :param company: A dictionary consisting of a company with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/companies.md#create-company
        :return: If the API call was successful the just created company will be returned
        """

        company = self._create_company(name, **kwargs)

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint='companies',
            data=company,
        )

    def update_company(self, company):
        """
        Updates a company.

        :param company: A dictionary consisting of a company with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/companies.md#create-company
        :return: If the API call was successful the just updated company will be returned
        """
        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'companies/{company.id}',
            data=company,
            params={'reload': 'true'}
        )

    def destroy_company(self, company):
        """
        Deletes a company.

        :param company: A dictionary consisting of a company with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/companies.md#create-company
        :return: The HTTP status code of the response of the DELETE request
        """
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'companies/{company.id}',
        )

    """
    Section: Notes
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/notes.md
    """

    def get_note(self, note_id):
        """
        Retrieves a single note by ID.

        :param note_id: The ID of the note in Highrise
        :return: A dictionary of the note
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'notes/{note_id}',
        )

    def get_comments_from_note(self, note_id):
        """
        Retrieves all the comments from a note.

        :param note_id: The ID of the note in Highrise
        :return: A list of dictionaries of comments
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'notes/{note_id}/comments',
        )

    def get_notes(self, subject_type, subject_id, since=None, page=0):
        """
        Retrieves the note/s of a subject, optionally since a certain date.

        :param subject_type: A type of any of these: ['companies', 'kases', 'deals', 'people']
        :param subject_id: The ID of the subject the note is added to
        :param since: A native Python datetime object
        :param page: Each page per 25 entries
        :return: A list of dictionaries of notes
        """
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/notes',
            params={
                'since': since.strftime('%Y%m%d%H%M%S') if since else None,
                'n': page * 25,
            },
        )

    def create_note(self, body, subject_id, subject_type):
        """
        Creates a new note.

        :param subject_type: A type of any of these: ['companies', 'kases', 'deals', 'people']
        :param subject_id: The ID of the subject to add the note to
        :param note: The content of the note
        :return: If the API call was successful the just created note will be returned
        """
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        note_object = etree.Element('note')
        id = etree.SubElement(note_object, 'body')
        id.text = body
        label = etree.SubElement(note_object, 'subject-id')
        label.text = str(subject_id)

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/notes',
            data=note_object,
        )

    def update_note(self, body, note_id):
        """
        Updates a note.

        :param note: A dictionary consisting of a note with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/notes.md#create-note
        :return: If the API call was successful the just updated note will be returned
        """
        note_object = etree.Element('note')
        id = etree.SubElement(note_object, 'body')
        id.text = body

        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'notes/{note_id}',
            data=note_object,
            params={'reload': 'true'}
        )

    def destroy_note(self, note):
        """
        Deletes a note.

        :param note: A dictionary consisting of a note with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/notes.md#create-note
        :return: The HTTP status code of the response of the DELETE request
        """
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'notes/{note.id}',
        )

    """
    Section: Tags
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/tags.md
    """

    def get_tags(self):
        """
        Retrieves all the tags.

        :return: A list of dictionaries of tags
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='tags',
        )

    def get_tags_by_subject(self, subject_type, subject_id):
        """
        Retrieves tags from a certain subject.

        :param subject_type: A type of any of these: ['companies', 'kases', 'deals', 'people']
        :param subject_id: The ID of the subject the tag is added to
        :return: A list of dictionaries of tags
        """
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/tags',
        )

    def get_tagged_parties(self, tag_id):
        """
        Return everything that is tagged with a certain tag.

        :param tag_id: The ID of the tag
        :return: A list of dictionaries of parties
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'tags/{tag_id}',
        )

    def add_tag(self, subject_type, subject_id, tag_name):
        """
        Adds a tag to a subject.

        :param subject_type: A type of any of these: ['companies', 'kases', 'deals', 'people']
        :param subject_id: The ID of the subject the tag is added to
        :param tag_name: The name of the tag to add as a string
        :return: If the API call was successful the just added tag will be returned
        """
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        tag = etree.Element('name')
        tag.text = tag_name

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/tags',
            data=tag,
            params={'reload': 'true'}
        )

    def remove_tag(self, subject_type, subject_id, tag_id):
        """
        Removes a tag from a subject.

        :param subject_type: A type of any of these: ['companies', 'kases', 'deals', 'people']
        :param subject_id: The ID of the subject the tag is added to
        :param tag_id: The ID of the tag
        :return: The HTTP status code of the response of the DELETE request
        """
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/tags/{tag_id}',
        )

    """
    Section: Custom Fields
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/custom_fields.md
    """

    CUSTOM_FIELD_TYPES = ['party', 'deal', 'all']

    def get_custom_fields(self, field_type):
        """
        Retrieves all the custom fields.

        :param field_type: A type of any of these: ['party', 'deal', 'all']
        :return: A list of dictionaries of custom fields
        """
        self._check_for_parameters(subject_type=field_type, types=Highton.CUSTOM_FIELD_TYPES)

        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='subject_fields',
            params=field_type
        )

    def create_party_custom_field(self, value):
        """
        Creates a new custom field.

        :param label: The name of the custom field
        :return: If the API call was successful the just added custom field will be returned
        """
        custom_field = etree.Element('subject-field')
        label = etree.SubElement(custom_field, 'label')
        label.text = value

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint='subject_fields',
            data=custom_field
        )

    def update_custom_field(self, field_type, custom_field_id, value):
        """
        Updates a custom field.

        :param field_type: A type of any of these: ['party', 'deal', 'all']
        :param custom_field_id: The ID of the custom field
        :param label: The new name for the chosen custom field
        :return:
        """
        self._check_for_parameters(subject_type=field_type, types=Highton.CUSTOM_FIELD_TYPES)

        custom_field = etree.Element('subject-field')
        id = etree.SubElement(custom_field, 'id')
        id.text = str(custom_field_id)
        label = etree.SubElement(custom_field, 'label')
        label.text = value
        type = etree.SubElement(custom_field, 'type')
        type.text = field_type

        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'subject_fields/{custom_field_id}',
            data=custom_field,
        )

    def destroy_custom_field(self, custom_field_id):
        """
        Deletes a custom field.

        :param custom_field_id: The ID of the custom field
        :return: The HTTP status code of the response of the DELETE request
        """
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'subject_fields/{custom_field_id}',
        )
