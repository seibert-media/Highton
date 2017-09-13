import xmltodict
import requests
from requests.auth import HTTPBasicAuth


class Highton:
    HIGHRISE_URL = 'highrisehq.com'

    def __init__(self, user, api_key):
        self._user = user
        self._api_key = api_key

    def _create_get_request(self, endpoint, params=None):
        return requests.get(
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=self._user,
                highrise_url=Highton.HIGHRISE_URL,
                endpoint=endpoint
            ),
            auth=HTTPBasicAuth(
                username=self._api_key,
                password=''
            ),
            params=params
        )

    def _create_post_request(self, endpoint, data=None):
        pass

    def _create_put_request(self, endpoint, data=None):
        pass

    def _create_delete_request(self, endpoint):
        pass

    def _parse_from_xml_to_dict(self, xml):
        pass

    def _parse_from_dict_to_xml(self, dic):
        pass

    def get_person(self, subject_id):
        self._create_get_request(
            endpoint='people/{}'.format(subject_id),
        )

    def get_people(self):
        pass
