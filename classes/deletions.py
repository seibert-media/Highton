from .tools import to_datetime


class Deletion(object):
    """
        Use:
        type
        deleted_at
        id
    """

    def save_data(self, deletion):

        self.highrise_id = deletion['id']
        self.deleted_at = to_datetime(deletion['deleted-at'])
        self.type = deletion['type']
