class HightonNotLoggedInException(Exception):
    def __str__(self):
        return 'You\'re not logged in, please init HightonSettings'

class HightonSettings:
    @staticmethod
    def return_valid_value_or_raise(value):
        if not value:
            raise HightonNotLoggedInException
        return value

    @classmethod
    def username(cls):
        return HightonSettings.return_valid_value_or_raise(cls.instance.username)

    @classmethod
    def api_key(cls):
        return HightonSettings.return_valid_value_or_raise(cls.instance.api_key)

    class __HightonSettings:
        def __init__(self, username, api_key):
            self.username = username
            self.api_key = api_key

    instance = None

    def __init__(self, username, api_key):
        if not HightonSettings.instance:
            HightonSettings.instance = HightonSettings.__HightonSettings(username, api_key)
        else:
            HightonSettings.instance.username = username
            HightonSettings.instance.api_key = api_key

    def __getattr__(self, name):
        value = getattr(self.instance, name)
        if not value:
            raise HightonNotLoggedInException
        return value