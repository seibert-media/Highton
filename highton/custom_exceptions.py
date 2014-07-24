

class HighriseRequestException(Exception):
    def __init__(self, function_name, message):
        self.function_name = function_name
        self.message = message

    def __unicode__(self):
        return 'Following type: {} threw following exception: {}'.format(
            self.function_name, self.message)


class ParseTimeException(Exception):
    def __init__(self, parsed_string):
        self.parsed_string = parsed_string

    def __unicode__(self):
        return 'Your parsed string: {} is false. Please correct it in ' \
            'following format: YYYYMMDDHHMMSS in Python you would ' \
            'say: %Y%m%d%H%M%S'


class FieldException(Exception):
    def __init__(self, fields):
        self.fields = fields

    def __unicode__(self):
        return 'You have to set the parameter on one of these fields: ' \
            '{}'.format(self.fields)


class XMLRequestException(Exception):
    def __init__(self, url):
        self.url = url

    def __unicode__(self):
        return 'Sorry but the url: {} doesnt response an xml.'.format(self.url)
