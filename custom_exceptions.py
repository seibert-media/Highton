

class HighriseGetException(Exception):
    def __init__(self, function_name, message):
        self.function_name = function_name
        self.message = message

    def __unicode__(self):
        return 'Following type: {} threw following exception: {}'.format(self.function_name, self.message)


class ParseTimeException(Exception):
    def __init__(self, parsed_string):
        self.parsed_string = parsed_string

    def __unicode__(self):
        return 'Your parsed string: {} is false. Please correct it in following format: YYYYMMDDHHMMSS in Python ' \
               'you would say: %Y%m%d%H%M%S'