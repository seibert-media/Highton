from highton.call_mixins import Call
from highton import fields


class SearchCallMixin(Call):
    """
    A mixin to search models

    """

    SEARCH_OFFSET = 25

    @classmethod
    def search(cls, term=None, page=0, **criteria):
        """
        Search a list of the model
        If you use "term":
        - Returns a collection of people that have a name matching the term passed in through the URL.

        If you use "criteria":
        - returns people who match your search criteria.
        Search by any criteria you can on the Contacts tab, including custom fields. Combine criteria to narrow results

        :param term: params as string
        :type term: str
        :param criteria: search for more criteria
        :type criteria: dict
        :param page: the page
        :type page: int
        :return: the list of the parsed xml objects
        :rtype: list
        """

        assert (term or criteria and not (term and criteria))

        params = {
            'n': int(page) * cls.SEARCH_OFFSET,
        }

        if term:
            params['term'] = term

        if criteria:
            for key, value in criteria.items():
                params['criteria[{}]'.format(key)] = value

        return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(
            cls.element_from_string(
                cls._get_request(
                    endpoint=cls.ENDPOINT + '/search',
                    params=params
                ).text
            )
        )
