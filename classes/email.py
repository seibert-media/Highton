from .attachment import Attachment
from .tools import to_datetime


class Email(object):
    def __init__(self):
        self.attachments = []

    def save_data(self, email):
        self.highrise_id = email['id'].pyval
        self.updated_at = to_datetime(email['updated-at'].pyval)
        self.created_at = to_datetime(email['created-at'].pyval)

        for attr in [
            'title',
            'body',
            'author-id',
            'subject-id',
            'subject-type',
            'subject-name',
            'collection-id',
            'collection-type',
            'visible-to',
            'owner-id',
            'group-id',
        ]:
            setattr(self, attr.replace('-', '_',), email[attr].pyval)

        if hasattr(email, 'attachments'):
            self.set_attachments(email['attachments'])

    def set_attachments(self, attachments):
        for attachment in attachments.getchildren():
            current_attachment = Attachment()
            current_attachment.save_data(attachment)
            self.attachments.append(current_attachment)
