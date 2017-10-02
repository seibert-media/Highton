from highton import fields, call_mixins
from highton.highton_constants import HightonConstants
from highton.models.contact import Contact


class Person(
    Contact,
    call_mixins.ListCallMixin,
):
    ENDPOINT = HightonConstants.PEOPLE
    TAG_NAME = HightonConstants.PERSON
    OFFSET = 500

    def __init__(self, **kwargs):
        self.company_id = fields.IntegerField(name=HightonConstants.COMPANY_ID)
        self.company_name = fields.StringField(name=HightonConstants.COMPANY_NAME)
        self.first_name = fields.StringField(name=HightonConstants.FIRST_NAME)
        self.last_name = fields.StringField(name=HightonConstants.LAST_NAME)
        self.title = fields.StringField(name=HightonConstants.TITLE)

        super().__init__(**kwargs)

    def list(self, page=None, since=None, tag_id=None, title=None):
        """
        
        :param page: page starting by 1 (not 0!!!)
        :type page: int
        :param since:
        :type since: datetime.datetime
        :param tag_id: id of a tag
        :type tag_id: int
        :param title: 
        :type title: str
        :return: 
        """
        params = {}
        if page:
            params['n'] = int(page) * self.OFFSET
        if since:
            params['since'] = since.strftime(self.COLLECTION_DATETIME)
        if tag_id:
            params['tag_id'] = str(tag_id)
        if title:
            params['title'] = title

        return super().list(params)





