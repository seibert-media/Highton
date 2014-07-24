from .tools import to_datetime


class Category(object):
    """
        Feel free to use these attributes, they will be added if you call
        get_task_categories in the Highton-Class:
        highrise_id,
        name,
    """
    def save_data(self, category):
        self.highrise_id = category['id'].pyval
        self.name = category['name'].pyval


class TaskCategory(Category):
    """
        This is just a class to identify later, which type of Category the
        request have. Feel free to use these attributes, they will be added
        if you call get_task_categories in the Highton-Class:
        highrise_id,
        name,
        updated_at,
        account_id,
        color,
        created_at,
        elements_count,
    """
    def save_data(self, category):
        self.highrise_id = category['id'].pyval

        self.created_at = to_datetime(category['created-at'].pyval)
        self.updated_at = to_datetime(category['updated-at'].pyval)
        for attr in [
            'name',
            'account-id',
            'color',
            'elements-count'
        ]:
            setattr(self, attr.replace('-', '_'), category[attr].pyval)


class DealCategory(Category):
    """
        This is just a class to identify later, which type of Category the
        request have. Feel free to use these attributes, they will be added
        if you call get_task_categories in the Highton-Class:
        highrise_id,
        name,
        updated_at,
        account_id,
        color,
        created_at,
        elements_count,
    """
    def save_data(self, category):
        self.highrise_id = category['id'].pyval
        self.created_at = to_datetime(category['created-at'].pyval)
        self.updated_at = to_datetime(category['updated-at'].pyval)

        for attr in [
            'name',
            'account-id',
            'color',
            'elements-count'
        ]:
            setattr(self, attr.replace('-', '_'), category[attr].pyval)
