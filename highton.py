# -*- coding: utf-8 -*-
import datetime

import requests
from lxml import objectify
from requests.auth import HTTPBasicAuth

from custom_exceptions import HighriseGetException, ParseTimeException, FieldException, XMLRequestException
from classes.person import Person
from classes.category import DealCategory, TaskCategory
from classes.company import Company
from classes.case import Case
from classes.deal import Deal
from classes.task import Task


class Highton(object):
    """
        Highton-API is just a really simple Python library which helps you to get information about your Highrise data
    """
    def __init__(self, api_key, user):
        self.user = user
        self.api_key = api_key
        self.api_key_password = 'X'

    def _request(self, endpoint, params={}):
        url = 'https://{}.highrisehq.com/{}.xml'.format(self.user, endpoint)
        request = requests.get(
            url,
            auth=HTTPBasicAuth(self.api_key, self.api_key_password),
            headers={'User-Agent': 'Highton-API: (bykof@me.com)'},
            params=params,
        )
        
        print request.content

        if 'text/html' in request.headers['content-type']:
            raise XMLRequestException(url)

        return request

    def _get_data(self, endpoint, params={}):
        data = []
        try:
            data = objectify.fromstring(
                self._request(endpoint, params).content
            ).getchildren()
        except TypeError:
            if not data:
                raise HighriseGetException(
                    endpoint,
                    'Parsing people from Highrise caused a failure'
                )
        return data

    def _get_paged_data(self, endpoint, params={}):
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

    def _get_object_data(self, data, highrise_class):
        data_list = []
        for d in data:
            temp = highrise_class()
            temp.save_data(d)
            data_list.append(temp)
        return data_list

    def get_people(self):
        """
        Just run this Method and you get a Person object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_object_data(self._get_paged_data('people'), Person)

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
        return self._get_object_data(self._get_paged_data('people', params={'since': since}), Person)

    def _get_categories(self, category_type):
        return self._get_data(category_type + '_categories')

    def get_task_categories(self):
        """
        Get all Task-Categories
        :return: all Task-Categories
        """
        return self._get_object_data(self._get_categories('task'), TaskCategory)

    def get_deal_categories(self):
        """
        Get all Deal-Categories
        :return: all Deal-Categories
        """
        return self._get_object_data(self._get_categories('deal'), DealCategory)

    def get_companies(self):
        """
        Just run this Method and you get a Company object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_object_data(self._get_paged_data('companies'), Company)

    def get_companies_since(self, since):
        """
        Gives you all companies since the set parameter
        :param since: string with %Y%m%d%H%M%S - Format
        :return: return all companies since the given parameter
        """
        try:
            datetime.datetime.strptime(since, '%Y%m%d%H%M%S')
        except ValueError:
            raise ParseTimeException
        return self._get_object_data(self._get_paged_data('companies', params={'since': since}), Company)

    def get_cases(self):
        """
        Just run this Method and you get a Case object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_object_data(self._get_paged_data('kases'), Case)

    def get_cases_since(self, since):
        """
        Gives you all Cases since the set parameter
        :param since: string with %Y%m%d%H%M%S - Format
        :return: return all cases since the given parameter
        """
        try:
            datetime.datetime.strptime(since, '%Y%m%d%H%M%S')
        except ValueError:
            raise ParseTimeException(since)
        return self._get_object_data(self._get_paged_data('kases', params={'since': since}), Case)

    def get_deals(self):
        """
        Gives you all Deals, but handle them wisely!
        :return: returns you all the Deals you have
        """
        return self._get_object_data(self._get_paged_data('deals'), Deal)

    def get_deals_since(self, since):
        """
        Gives you all deals since the parameter since
        :param since: Have to be String in format YYYYMMDDHHMMSS
        :return: returns you all Deals which were updated since the parameter
        """
        try:
            datetime.datetime.strptime(since, '%Y%m%d%H%M%S')
        except ValueError:
            raise ParseTimeException
        return self._get_object_data(self._get_paged_data('deals', params={'since': since}), Deal)

    def get_deals_by_status(self, status):
        fields = ['won', 'lost', 'pending']
        if status not in fields:
            raise FieldException(fields)
        return self._get_object_data(self._get_paged_data('deals', params={'status': status}), Deal)

    def _get_tasks(self, subject_id, highrise_type):
        return self._get_object_data(self._get_data('{}/{}/tasks'.format(highrise_type, subject_id)), Task)

    def get_person_tasks(self, subject_id):
        return self._get_tasks(subject_id, 'people')

    def get_company_tasks(self, subject_id):
        return self._get_tasks(subject_id, 'companies')

    def get_case_tasks(self, subject_id):
        return self._get_tasks(subject_id, 'kases')

    def get_deal_tasks(self, subject_id):
        return self._get_tasks(subject_id, 'deals')

