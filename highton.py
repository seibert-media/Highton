import logging
import xmltodict
import requests
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)


class Highton:
    GET_REQUEST = 'GET'
    POST_REQUEST = 'POST'
    PUT_REQUEST = 'PUT'
    DELETE_REQUEST = 'DELETE'
    HIGHRISE_URL = 'highrisehq.com'

    class RequestException(Exception):
        pass

    def __init__(self, user, api_key):
        """
        :param user: Your personal username for the Highrise API
        :param api_key: Your personal API-Key for the Highrise API
        """
        self._user = user
        self._api_key = api_key

    @staticmethod
    def _parse_from_xml_to_dict(xml):
        return xmltodict.parse(xml)

    @staticmethod
    def _parse_from_dict_to_xml(dictionary):
        return xmltodict.unparse(dictionary)

    def _send_request(self, method, endpoint, params=None, data=None):
        response = requests.request(
            method=method,
            url=f'https://{self._user}.{Highton.HIGHRISE_URL}/{endpoint}.xml',
            headers={'Content-Type': 'application/xml'},
            auth=HTTPBasicAuth(username=self._api_key, password=''),
            params=params if params else {},
            data=data,
        )

        if not response.ok:
            raise Highton.RequestException(response.status_code)
        else:
            return response

    def _create_request(self, method, endpoint, params=None, data=None):
        try:
            return self._parse_from_xml_to_dict(
                self._send_request(
                    method=method,
                    endpoint=endpoint,
                    params=params,
                    data=self._parse_from_dict_to_xml(data)
                ).content
            )
        except Highton.RequestException as e:
            logger.error(
                f'The {method}-request towards the endpoint "/{endpoint}.xml" failed with HTTP-Code {str(e)}'
            )
