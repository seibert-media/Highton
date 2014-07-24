from .tools import to_datetime


class Task(object):
    """
        Feel free to use these attributes:
        highrise_id
        recording-id
        subject-id
        subject-type
        category-id
        body
        frame
        due-at
        alert-at
        created-at
        author-id
        updated-at
        public
        recording-id
        subject-id
        subject-type
        category-id
        body
        frame
        due-at
        alert-at
        created-at
        author-id
        updated-at
        public
    """

    def save_data(self, task):
        self.highrise_id = task['id'].pyval
        self.created_at = to_datetime(task['created-at'].pyval)
        self.updated_at = to_datetime(task['updated-at'].pyval)
        self.due_at = to_datetime(task['due-at'].pyval)
        self.alert_at = to_datetime(task['alert-at'].pyval)

        for attr in [
            'recording-id',
            'subject-id',
            'subject-type',
            'subject-name',
            'category-id',
            'body',
            'frame',
            'author-id',
            'public',
            'recording-id',
        ]:
            setattr(self, attr.replace('-', '_'), task[attr].pyval)
