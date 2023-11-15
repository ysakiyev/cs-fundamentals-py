from unittest import TestCase
from hash_map import HashMap


class TestHashMap(TestCase):
    def setUp(self):
        self.ll = HashMap()

    def test_set(self):
        self.ll.set('key1', 'val1')
        self.ll.set('key2', 'val2')
        self.ll.set('key3', 'val3')

        res1 = self.ll.get('key1')
        res2 = self.ll.get('key2')
        res3 = self.ll.get('key3')
        self.assertEqual('val1', res1)
        self.assertEqual('val2', res2)
        self.assertEqual('val3', res3)

    def test_get(self):
        self.ll.set('key1', 'val1')
        res1 = self.ll.get('key1')
        self.assertEqual('val1', res1)

    def test_rm(self):
        self.ll.set('key1', 'val1')
        self.ll.set('key2', 'val2')
        self.ll.set('key3', 'val3')
        self.ll.rm('key1')
        res1 = self.ll.get('key1')
        self.assertEqual(None, res1)

