# -*- coding: utf-8 -*-
import datetime

import requests
from lxml import objectify
from requests.auth import HTTPBasicAuth

from custom_exceptions import HighriseGetException, ParseTimeException
from classes.person import Person
from classes.task_category import DealCategory, TaskCategory
from classes.company import Company
from classes.case import Case


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

    def _get_person_objects(self, people):
        return_people = []
        for person in people:
            temp_person = Person()
            temp_person.save_data(person)
            return_people.append(temp_person)
        return return_people

    def get_people(self):
        """
        Just run this Method and you get a Person object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_person_objects(self._get_paged_data('people'))

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
        return self._get_person_objects(self._get_paged_data('people', params={'since': since}))

    def _get_categories(self, category_type):
        return self._get_data(category_type + '_categories')

    def _get_category_objects(self, categories, category_type):
        return_categories = []
        for category in categories:
            if category_type == 'task':
                temp_category = TaskCategory()
            elif category_type == 'deal':
                temp_category = DealCategory()
            temp_category.save_data(category)
            return_categories.append(temp_category)
        return return_categories

    def get_task_categories(self):
        category_type = 'task'
        return self._get_category_objects(self._get_categories(category_type), category_type)

    def get_deal_categories(self):
        category_type = 'deal'
        return self._get_category_objects(self._get_categories(category_type), category_type)

    def _get_company_objects(self, companies):
        return_companies = []
        for company in companies:
            temp_company = Company()
            temp_company.save_data(company)
            return_companies.append(temp_company)
        return return_companies

    def get_companies(self):
        """
        Just run this Method and you get a Company object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_company_objects(self._get_paged_data('companies'))

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
        return self._get_company_objects(self._get_paged_data('companies', params={'since': since}))

    def _get_case_objects(self, cases):
        return_cases = []
        for case in cases:
            temp_case = Case()
            temp_case.save_data(case)
            return_cases.append(temp_case)
        return return_cases

    def get_cases(self):
        """
        Just run this Method and you get a Case object with all objects and attributes inside it. Get Lucky
        :return: returns all people (of course it iterates over all pages, so you dont get only the first 500)
        """
        return self._get_case_objects(self._get_paged_data('kases'))

    def get_cases_since(self, since):
        """
        Gives you all Cases since the set parameter
        :param since: string with %Y%m%d%H%M%S - Format
        :return: return all cases since the given parameter
        """
        try:
            datetime.datetime.strptime(since, '%Y%m%d%H%M%S')
        except ValueError:
            raise ParseTimeException
        return self._get_case_objects(self._get_paged_data('kases', params={'since': since}))
