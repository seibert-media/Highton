import logging

import requests
import xmltodict
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
        """ Offers an Exception in case of a request that timed-out, failed or was malformed """
        pass

    class InsufficentParametersException(Exception):
        """ Offers an Exception in case of a method call that did not receive the correct parameters """
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
    def _parse_from_xml_to_dict(xml):
        """
        Parses valid XML into native Python dictionaries with the ability to parse them back into XML later on.

        :param xml: Valid XML as a string
        :return: A Python dictionary
        """
        return xmltodict.parse(xml)

    @staticmethod
    def _parse_from_dict_to_xml(dictionary):
        """
        Parses a native Python dictionary into valid XML.

        :param dictionary: A Python dictionary
        :return: Valid XML as a string
        """
        return xmltodict.unparse(dictionary)

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
                data=self._parse_from_dict_to_xml(data) if data else {}
            )

            if len(response.content) > 1:
                return self._parse_from_xml_to_dict(response.content)
            else:
                return response.status_code
        except Highton.RequestException as e:
            logger.error(
                f'The {method}-request towards the endpoint "/{endpoint}.xml" failed with HTTP-Code {str(e)}'
            )

    def _check_for_parameters(self, subject_type, types):
        """
        Is used within many API methods to check if a correct 'subject_type' was selected.
        It raises an Exception otherwise.

        :param subject_type: The type to check against
        :param types: A list of types to check for
        """
        if subject_type not in types:
            raise Highton.InsufficentParametersException(f'The parameter subject must be in {types}')

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
        ).get('people').get('person', [])

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
        ).get('people').get('person', [])

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
        ).get('people').get('person', [])

    def get_people_of_company(self, company):
        """
        Retrieves people that belong to a certain company

        :param company: The company as a dictionary preferrably returned from an earlier API call
        :return: A list of dictionaries of people
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'companies/{company["id"]["#text"]}/people',
        ).get('people').get('person', [])

    def get_person(self, subject_id):
        """
        Retrieves a single person by ID.

        :param subject_id: The ID of the person in Highrise
        :return: A dictionary of the person
        """
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'people/{subject_id}',
        ).get('person', {})

    def create_person(self, person):
        """
        Creates a new person.

        :param person: A dictionary consisting of a person with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/people.md#create-person
        :return: If the API call was successful the just created person will be returned
        """
        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint='people',
            data=person if person.get('person') else {'person': person},
        ).get('person', {})

    def update_person(self, person):
        """
        Updates a person.

        :param person: A dictionary consisting of a person with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/people.md#create-person
        :return: If the API call was successful the just created person will be returned
        """
        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'people/{person["id"]["#text"]}',
            data={
                'person': person,
                'reload': 'true',
            },
        ).get('person', {})

    def destroy_person(self, person):
        """
        Deletes a person.

        :param person: A dictionary consisting of a person with this formatting as a native Python dictionary:
        https://github.com/basecamp/highrise-api/blob/master/sections/people.md#create-person
        :return: The HTTP status code of the DELETE request
        """
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'people/{person.get("id").get("#text")}',
        )

    """
    Section: Companies
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/companies.md
    """

    def get_companies(self, since, page=0):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='companies',
            params={
                'since': since.strftime('%Y%m%d%H%M%S') if since else None,
                'n': page * 500,
            }
        ).get('companies').get('company', [])

    def get_companies_by_tag(self, tag_id):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'companies',
            params={
                'tag_id': tag_id,
            }
        ).get('companies').get('company', [])

    def search_companies(self, term=None, page=0, **criteria):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='companies/search',
            params={
                **{f'criteria[{k}]': v for k, v in criteria.items()},
                **{'n': page * 25},
                **{'term': term},
            },
        ).get('companies').get('company', [])

    def get_company(self, subject_id):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'companies/{subject_id}',
        ).get('company', {})

    def create_company(self, company):
        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint='companies',
            data=company if company.get('company') else {'company': company},
        ).get('company', {})

    def update_company(self, company):
        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'companies/{company["id"]["#text"]}',
            data={
                'company': company,
                'reload': 'true',
            },
        ).get('company', {})

    def destroy_company(self, company):
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'companies/{company["id"]["#text"]}',
        )

    """
    Section: Notes
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/notes.md
    """

    def get_note(self, note_id):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'notes/{note_id}',
        ).get('note', {})

    def get_comments_from_note(self, note_id):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'notes/{note_id}/comments',
        ).get('comments').get('comment', [])

    def get_notes(self, subject_type, subject_id, since=None, page=0):
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/notes',
            params={
                'since': since.strftime('%Y%m%d%H%M%S'),
                'n': page * 25,
            },
        ).get('notes').get('note', [])

    def create_note(self, subject_type, subject_id, note):
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/notes',
            data=note if note.get('note') else {'note': note},
        ).get('note', {})

    def update_note(self, note):
        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'notes/{note["id"]["#text"]}',
            data={
                'note': note,
                'reload': 'true',
            },
        ).get('note', {})

    def destroy_note(self, note):
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'notes/{note["id"]["#text"]}',
        )

    """
    Section: Tags
    Docs: https://github.com/basecamp/highrise-api/blob/master/sections/tags.md
    """

    def get_tags(self):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='tags',
        ).get('tags').get('tag', [])

    def get_tags_by_subject(self, subject_type, subject_id):
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/tags',
        ).get('tags').get('tag', [])

    def get_tagged_parties(self, tag_id):
        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint=f'tags/{tag_id}',
        ).get('parties').get('party', [])

    def add_tag(self, subject_type, subject_id, tag_name):
        self._check_for_parameters(subject_type=subject_type, types=Highton.SUBJECT_TYPES)

        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint=f'{subject_type}/{subject_id}/tags',
            data={'name': tag_name},
        ).get('tag', {})

    def remove_tag(self, subject_type, subject_id, tag_id):
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
        self._check_for_parameters(subject_type=field_type, types=Highton.CUSTOM_FIELD_TYPES)

        return self._make_request(
            method=Highton.GET_REQUEST,
            endpoint='subject_fields',
            params={'type': field_type}
        ).get('subject-fields').get('subject-field', [])

    def create_party_custom_field(self, label):
        return self._make_request(
            method=Highton.POST_REQUEST,
            endpoint='subject_fields',
            data={'subject-field': {'label': label}},
        ).get('subject-field', {})

    def update_custom_field(self, field_type, custom_field_id, label):
        self._check_for_parameters(subject_type=field_type, types=Highton.CUSTOM_FIELD_TYPES)

        return self._make_request(
            method=Highton.PUT_REQUEST,
            endpoint=f'subject_fields/{custom_field_id}',
            data={'subject-field':{'id': custom_field_id, 'label': label, 'type': field_type}},
        )

    def destroy_custom_field(self, custom_field_id):
        return self._make_request(
            method=Highton.DELETE_REQUEST,
            endpoint=f'subject_fields/{custom_field_id}',
        )
