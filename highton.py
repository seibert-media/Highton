import xmltodict
import requests
from requests.auth import HTTPBasicAuth


class Highton:
    HIGHRISE_URL = 'highrisehq.com'

    def __init__(self, user, api_key):
        self._user = user
        self._api_key = api_key

    @staticmethod
    def _parse_from_xml_to_dict(xml):
        return xmltodict.parse(xml)

    @staticmethod
    def _parse_from_dict_to_xml(dictionary):
        return xmltodict.unparse(dictionary)

    def _create_get_request(self, endpoint, params=None):
        get_response = requests.get(
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=self._user,
                highrise_url=Highton.HIGHRISE_URL,
                endpoint=endpoint
            ),
            auth=HTTPBasicAuth(
                username=self._api_key,
                password=''
            ),
            params=params if params else {},
        )

        return self._parse_from_xml_to_dict(get_response.content)

    def _create_post_request(self, endpoint, data):
        post_response = requests.post(
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=self._user,
                highrise_url=Highton.HIGHRISE_URL,
                endpoint=endpoint
            ),
            auth=HTTPBasicAuth(
                username=self._api_key,
                password=''
            ),
            headers={'Content-Type': 'application/xml'},
            data=self._parse_from_dict_to_xml(data),
        )

        return self._parse_from_xml_to_dict(post_response.content)

    def _create_put_request(self, endpoint, data):
        put_response = requests.put(
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=self._user,
                highrise_url=Highton.HIGHRISE_URL,
                endpoint=endpoint
            ),
            auth=HTTPBasicAuth(
                username=self._api_key,
                password=''
            ),
            headers={'Content-Type': 'application/xml'},
            data=self._parse_from_dict_to_xml(data),
        )

        return put_response.text

    def _create_delete_request(self, endpoint):
        delete_response = requests.delete(
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=self._user,
                highrise_url=Highton.HIGHRISE_URL,
                endpoint=endpoint
            ),
            auth=HTTPBasicAuth(
                username=self._api_key,
                password=''
            ),
        )

        return delete_response.ok

    def get_person(self, subject_id):
        return self._create_get_request(
            endpoint='people/{}'.format(subject_id),
        )

    def get_people(self):
        pass
