class HightonConstants:
    # is used for requests
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    HIGHRISE_URL = 'highrisehq.com'

    # Company
    COMPANIES = 'companies'
    COMPANY = 'company'
    COMPANY_NAME = 'company-name'
    COMPANY_ID = 'company-id'

    # Case
    KASES = 'kases'

    # Deal
    DEALS = 'deals'

    # Person
    PEOPLE = 'people'
    PERSON = 'person'

    NAME = 'name'
    TITLE = 'title'
    FIRST_NAME = 'first-name'
    LAST_NAME = 'last-name'
    CONTACT_DATA = 'contact-data'

    EMAIL_ADDRESS = 'email-address'
    EMAIL_ADDRESSES = 'email-addresses'

    WEB_ADDRESS = 'web-address'
    WEB_ADDRESSES = 'web-addresses'

    PHONE_NUMBER = 'phone-number'
    PHONE_NUMBERS = 'phone-numbers'

    SUBJECT_DATA = 'subject_data'
    SUBJECT_DATAS = 'subject_datas'

    ADDRESS = 'address'
    ADDRESSES = 'addresses'

    NOTE = 'note'
    NOTES = 'notes'

    TAG = 'tag'
    TAGS = 'tags'

    SUBJECT_ID = 'subject-id'
    SUBJECT_FIELD = 'subject-field'
    SUBJECT_FIELDS = 'subject_fields'
    SUBJECT_FIELD_ID = 'subject_field_id'

    URL = 'url'
    ZIP = 'zip'
    CITY = 'city'
    STREET = 'street'
    NUMBER = 'number'
    COUNTRY = 'country'
    LOCATION = 'location'

    ID = 'id'
    BODY = 'body'
    TYPE = 'type'
    VALUE = 'value'
    LABEL = 'label'
    SEARCH = 'search'
    COMMENTS = 'comments'
    BACKGROUND = 'background'

    ALL = 'all'
    DEAL = 'deal'
    PARTY = 'party'

    SUBJECT_TYPES = [COMPANIES, KASES, DEALS, PEOPLE, ]
    CUSTOM_FIELD_TYPES = [PARTY, DEAL, ALL, ]