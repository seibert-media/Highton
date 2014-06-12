# -*- coding: utf-8 -*-
import datetime

import requests
from lxml import objectify
from requests.auth import HTTPBasicAuth

from custom_exceptions import HighriseGetException, ParseTimeException
from classes.person import *


class Highton(object):
    """
        Highton-API is just a really simple Python library which helps you to get information about your Highrise data
    """
    def __init__(self, api_key, user):
        self.user = user
        self.api_key = api_key
        self.api_key_password = 'X'

    def _request(self, endpoint, params={}):
        return requests.get(
            'https://{}.highrisehq.com/{}.xml'.format(self.user, endpoint),
            auth=HTTPBasicAuth(self.api_key, self.api_key_password),
            headers={'User-Agent': 'Highton-API: (bykof@me.com)', 'Content-Type': 'application/xml'},
            params=params,
        )

    def _get_data(self, endpoint, params={}):
        data = []
        try:
            page = 500
            counter = 0
            while True:
                params.update({'n': page * counter})
                objects = objectify.fromstring(
                    self._request(endpoint, params).content
                ).getchildren()

                if objects:
                    data += objects
                else:
                    break
                counter += 1
        except TypeError:
            if not data:
                raise HighriseGetException(
                    endpoint,
                    'Parsing people from Highrise caused a failure'
                )
        return data

    def _get_person_objects(self, people):
        return_people = []
        for person in people:
            temp_person = Person()
            temp_person.highrise_id = person['id']

            for attr in [
                'first-name',
                'last-name',
                'title',
                'background',
                'linkedin-url',
                'avatar-url',
                'company-id',
                'company-name',
                'created-at',
                'updated-at',
                'visible-to',
                'owner-id',
                'group-id',
                'author-id',
            ]:
                setattr(temp_person, attr.replace('-', '_'), person[attr])

            for attr in [
                'phone-numbers',
                'email-addresses',
                'addresses',
            ]:
                if hasattr(person['contact-data'], attr):
                    getattr(temp_person, 'set_' + attr.replace('-', '_'))(person['contact-data'][attr])

            for attr in [
                'subject_datas',
                'tags',
            ]:
                if hasattr(person, attr):
                    getattr(temp_person, 'set_' + attr.replace('-', '_'))(person[attr])

            return_people.append(temp_person)
        return return_people

    def get_people(self):
        """
        Just run this Method and you get a Person object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_person_objects(self._get_data('people'))

    def get_people_since(self, since):
        """
        Gives you all people since the set parameter
        :param since: string with %Y%m%d%H%M%S - Format
        :return: return all people since the given parameter
        """
        try:
            datetime.datetime.strptime(since, '%Y%m%d%H%M%S')
        except ValueError:
            raise ParseTimeException

        return self._get_person_objects(self._get_data('people', params={'since': since}))