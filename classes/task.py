

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
        self.highrise_id = task['id']

        for attr in [
            'recording-id',
            'subject-id',
            'subject-type',
            'category-id',
            'body',
            'frame',
            'due-at',
            'alert-at',
            'created-at',
            'author-id',
            'updated-at',
            'public',
            'recording-id',
            'subject-id',
            'subject-type',
            'category-id',
            'body',
            'frame',
            'due-at',
            'alert-at',
            'created-at',
            'author-id',
            'updated-at',
            'public']:
            setattr(self, attr.replace('-', '_'), task[attr])
