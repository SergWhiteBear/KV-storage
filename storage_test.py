import unittest
import os
from storage import KeyValueStorage


class TestKVStorage(unittest.TestCase):

    def setUp(self):
        self.storage_name = "test_file.json"
        self.storage = KeyValueStorage(self.storage_name)

    def tearDown(self):
        self.storage.close()
        os.remove(self.storage_name)

    def test_set_get_item(self):
        self.storage['key1'] = 'value1'
        self.assertEqual(self.storage['key1'], 'value1')

    def test_get_nonexist_key(self):
        with self.assertRaises(KeyError):
            value = self.storage['nonexist_key']

    def test_del_item(self):
        self.storage['del_key'] = 'del_value'
        del self.storage['del_key']
        with self.assertRaises(KeyError):
            value = self.storage['del_key']

    def test_del_nonexist_item(self):
        with self.assertRaises(KeyError):
            del self.storage['nonexist_key']

    def test_get_all_keys(self):
        self.storage['key1'] = 'value1'
        self.storage['key2'] = 'value2'
        self.assertEqual(self.storage.get_all_keys(), ['key1', 'key2'])

    def test_search_value(self):
        self.storage['key1'] = 'value1'
        self.storage['key2'] = 'value2'
        self.assertEqual(self.storage.search_value('value1'), 'key1')

    def test_search_nonexist_value(self):
        self.storage['key1'] = 'value1'
        self.storage['key2'] = 'value2'
        with self.assertRaises(ValueError):
            key = self.storage.search_value("nonexistent_value")


if __name__ == '__main__':
    unittest.main()

