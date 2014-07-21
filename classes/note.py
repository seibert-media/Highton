from .attachment import Attachment
from .tools import to_datetime


class Note(object):
    """
        highrise_id
        body
        author_id
        subject_id
        subject_type
        subject_name
        collection_id
        collection_type
        visible_to
        owner_id
        group_id
        updated_at
        created_at
        attachments
    """
    def __init__(self):
        self.attachments = []

    def save_data(self, note):
        self.highrise_id = note['id'].pyval
        self.created_at = to_datetime(note['created-at'].pyval)
        self.updated_at = to_datetime(note['updated-at'].pyval)

        for attr in [
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
            setattr(self, attr.replace('-', '_',), note[attr].pyval)

        if hasattr(note, 'attachments'):
            self.set_attachments(note['attachments'])

    def set_attachments(self, attachments):
        for attachment in attachments.getchildren():
            current_attachment = Attachment()
            current_attachment.save_data(attachment)
            self.attachments.append(current_attachment)
