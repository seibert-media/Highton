from abc import ABCMeta

import requests
from requests.auth import HTTPBasicAuth

from highton.highton_constants import HightonConstants
from highton.highton_settings import HightonSettings

class Call(metaclass=ABCMeta):
    ENDPOINT = None
    COLLECTION_DATETIME = '%Y%m%d%H%M%S'

    # yyyymmddhhmmss

    @classmethod
    def _request(cls, method, endpoint=None, params=None, data=None, endpoint_suffix='.xml'):
        response = requests.request(
            method=method,
            url='https://{user}.{highrise_url}/{endpoint}{endpoint_suffix}'.format(
                user=HightonSettings.username(),
                highrise_url=HightonConstants.HIGHRISE_URL,
                endpoint=endpoint if endpoint else cls.ENDPOINT,
                endpoint_suffix=endpoint_suffix
            ),
            headers={'Content-Type': 'application/xml'},
            auth=HTTPBasicAuth(username=HightonSettings.api_key(), password=''),
            params=params,
            data=data,
        )
        response.raise_for_status()
        return response

    @classmethod
    def _get_request(cls, endpoint=None, params=None, endpoint_suffix='.xml'):
        return cls._request(method=HightonConstants.GET, endpoint=endpoint, params=params, endpoint_suffix=endpoint_suffix)

    @classmethod
    def _post_request(cls, data, endpoint=None, params=None):
        return cls._request(method=HightonConstants.POST, endpoint=endpoint, params=params, data=data)

    @classmethod
    def _put_request(cls, data, endpoint=None, params=None):
        return cls._request(method=HightonConstants.PUT, endpoint=endpoint, params=params, data=data)

    @classmethod
    def _delete_request(cls, endpoint=None, params=None):
        return cls._request(method=HightonConstants.DELETE, endpoint=endpoint, params=params)
