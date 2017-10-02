import datetime
import unittest
from xml.etree import ElementTree

from highton import fields
from highton.models import HightonModel

TEST_CLASS_XML = b'<test><id type="integer">1</id><name>NAME</name><created-date type="date">2007-03-19</created-date><created-datetime type="date">2007-03-19T22:34:22Z</created-datetime><tags type="array"><tag><id>1</id><name>#1</name></tag><tag><id>2</id><name>#2</name></tag></tags><category><id>123</id><value>test</value></category></test>'

TEST_CLASS_XML_WITH_NONE = b'<test-with-none><id nil="true"/></test-with-none>'

FIELD_DOES_NOT_EXIST_TEST_CLASS_XML = """
<test>
    <does-not-exist>NAME</does-not-exist>
</test>
"""


class Tag(HightonModel):
    TAG_NAME = 'tag'

    def __init__(self, **kwargs):
        self.name = fields.StringField(name='name')
        super().__init__(**kwargs)


class Category(HightonModel):
    TAG_NAME = 'category'

    def __init__(self, **kwargs):
        self.value = fields.StringField(name='value')
        super().__init__(**kwargs)


class TestClass(HightonModel):
    TAG_NAME = 'test'

    def __init__(self, **kwargs):
        self.name = fields.StringField(name='name')
        self.created_date = fields.DateField(name='created-date')
        self.created_datetime = fields.DatetimeField(name='created-datetime')
        self.tags = fields.ListField(name='tags', init_class=Tag)
        self.category = fields.ObjectField(name='category', init_class=Category)
        super().__init__(**kwargs)

class TestWithNone(HightonModel):
    TAG_NAME = 'test-with-none'


class TestXMLEncoder(unittest.TestCase):
    def test_encode(self):
        test_class = TestClass(
            id=1,
            name='NAME',
            created_date=datetime.datetime(2007, 3, 19).date(),
            created_datetime=datetime.datetime(2007, 3, 19, 22, 34, 22),
            tags=[
                Tag(id=1, name='#1'),
                Tag(id=2, name='#2')
            ],
            category=Category(id=123, value='test')
        )

        self.assertEqual(
            set(test_class.encode().itertext()),
            set(ElementTree.fromstring(TEST_CLASS_XML).itertext())
        )

    def test_with_none(self):
        test_with_none_class = TestWithNone(id=None)

        self.assertEqual(
            set(test_with_none_class.encode().itertext()),
            set(ElementTree.fromstring(TEST_CLASS_XML_WITH_NONE).itertext())
        )



