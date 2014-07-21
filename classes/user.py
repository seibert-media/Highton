from .tools import to_datetime


class User(object):
    """
        Feel free to use these attributes:
        highrise_id
        name
        email_address
        created_at
        updated_at
        admin
    """

    def save_data(self, user):
        self.highrise_id = user['id'].pyval
        self.created_at = to_datetime(user['created-at'].pyval)
        self.updated_at = to_datetime(user['updated-at'].pyval)

        for attr in [
            'name',
            'email-address',
            'admin'
        ]:
            setattr(self, attr.replace('-', '_'), user[attr].pyval)
