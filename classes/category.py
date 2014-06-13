

class Category(object):
    """
        Feel free to use these attributes, they will be added if you call get_task_categories in the Highton-Class
        highrise_id,
        name,
    """
    def save_data(self, category):
        self.highrise_id = category['id']
        self.name = category['name']


class TaskCategory(Category):
    """
        This is just a class to identify later, which type of Category the request have
        Feel free to use these attributes, they will be added if you call get_task_categories in the Highton-Class
        highrise_id,
        name,
        updated_at,
        account_id,
        color,
        created_at,
        elements_count,
    """
    def save_data(self, category):
        self.highrise_id = category['id']

        for attr in [
            'name',
            'updated-at',
            'account-id',
            'color',
            'created-at',
            'elements-count'
        ]:
            setattr(self, attr.replace('-', '_'), category[attr])


class DealCategory(Category):
    """
        This is just a class to identify later, which type of Category the request have
        Feel free to use these attributes, they will be added if you call get_task_categories in the Highton-Class
        highrise_id,
        name,
        updated_at,
        account_id,
        color,
        created_at,
        elements_count,
    """
    def save_data(self, category):
        self.highrise_id = category['id']

        for attr in [
            'name',
            'updated-at',
            'account-id',
            'color',
            'created-at',
            'elements-count'
        ]:
            setattr(self, attr.replace('-', '_'), category[attr])