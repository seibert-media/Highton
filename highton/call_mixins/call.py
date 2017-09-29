from abc import ABCMeta

import requests
from requests.auth import HTTPBasicAuth

from highton.highton_constants import HightonConstants
from highton.highton_settings import USERNAME, API_KEY


class Call(metaclass=ABCMeta):
    ENDPOINT = None

    @classmethod
    def _request(cls, method, params=None, data=None):
        return requests.request(
            method=method,
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=USERNAME,
                highrise_url=HightonConstants.HIGHRISE_URL,
                endpoint=cls.ENDPOINT
            ),
            headers={'Content-Type': 'application/xml'},
            auth=HTTPBasicAuth(username=API_KEY, password=''),
            params=params,
            data=data,
        )

    @classmethod
    def _get_request(cls, params):
        return cls._request(method=HightonConstants.GET, params=params)

    @classmethod
    def _post_request(cls, params, data):
        return cls._request(method=HightonConstants.POST, params=params, data=data)

    @classmethod
    def _put_request(cls, params, data):
        return cls._request(method=HightonConstants.PUT, params=params, data=data)

    @classmethod
    def _delete_request(cls, params):
        return cls._request(method=HightonConstants.DELETE, params=params)
