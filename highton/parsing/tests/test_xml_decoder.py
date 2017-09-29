import datetime
import unittest
from xml.etree import ElementTree

from highton import fields
from highton.models import HightonModel
from highton.parsing.xml_decoder import FieldDoesNotExist

TEST_CLASS_XML = """
<test>
    <id type="integer">1</id>
    <name>NAME</name>
    <created-date type="date">2007-03-19</created-date>
    <created-datetime type="date">2007-03-19T22:34:22Z</created-datetime>
    <tags type="array">
        <tag>
            <id>1</id>
            <name>#1</name>
        </tag>
        <tag>
            <id>2</id>
            <name>#2</name>
        </tag>
    </tags>
     <category>
        <id>123</id>
        <value>test</value>
    </category>
</test>
"""

FIELD_DOES_NOT_EXIST_TEST_CLASS_XML = """
<test>
    <does-not-exist>NAME</does-not-exist>
</test>
"""


class Tag(HightonModel):
    def __init__(self, **kwargs):
        self.name = fields.StringField(name='name')
        super().__init__(**kwargs)

class Category(HightonModel):
    def __init__(self, **kwargs):
        self.id = fields.IntegerField(name='id')
        self.value = fields.StringField(name='value')
        super().__init__(**kwargs)

class TestClass(HightonModel):
    def __init__(self, **kwargs):
        self.name = fields.StringField(name='name')
        self.created_date = fields.DateField(name='created-date')
        self.created_datetime = fields.DatetimeField(name='created-datetime')
        self.tags = fields.ListField(name='tags', init_class=Tag)
        self.category = fields.ObjectField(name='category', init_class=Category)
        super().__init__(**kwargs)


class TestXMLDecoder(unittest.TestCase):
    def test_decode(self):
        test_class = TestClass.decode(ElementTree.fromstring(TEST_CLASS_XML))
        self.assertEqual(test_class.id, 1)
        self.assertEqual(test_class.name, 'NAME')
        self.assertEqual(test_class.created_date, datetime.datetime(2007, 3, 19).date())
        self.assertEqual(test_class.created_datetime, datetime.datetime(2007, 3, 19, 22, 34, 22))
        self.assertEqual(
            test_class.tags[0].id,
            1
        )
        self.assertEqual(
            test_class.tags[0].name,
            '#1'
        )
        self.assertEqual(
            test_class.tags[1].id,
            2
        )
        self.assertEqual(
            test_class.tags[1].name,
            '#2'
        )
        self.assertEqual(
            test_class.category.id,
            123
        )
        self.assertEqual(
            test_class.category.value,
            'test'
        )

    def test_field_does_not_exist(self):
        with self.assertRaises(FieldDoesNotExist):
            TestClass.decode(ElementTree.fromstring(FIELD_DOES_NOT_EXIST_TEST_CLASS_XML))
