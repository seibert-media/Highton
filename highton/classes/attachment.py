

class Attachment(object):
    """
        highrise_id
        url
        name
        size
    """
    def save_data(self, attachment):
        self.highrise_id = attachment['id'].pyval

        for attr in ['url', 'name', 'size']:
            setattr(self, attr, attachment[attr].pyval)