from unittest import TestCase
from trie import Trie


class TestTrie(TestCase):
    def setUp(self):
        self.t = Trie()
        self.t.insert("app")
        self.t.insert("apple")
        self.t.insert("beer")
        self.t.insert("add")
        self.t.insert("jam")
        self.t.insert("rental")

    def test_search(self):
        tests = {
            "apps": False,
            "app": True,
            "ad": False,
            "applepie": False,
            "rest": False,
            "jan": False,
            "rent": False,
            "beer": True,
            "jam": True,
        }

        for test_word, expected in tests.items():
            self.assertEqual(expected, self.t.search(test_word))

    def test_starts_with(self):
        tests = {
            "apps": False,
            "app": True,
            "ad": True,
            "applepie": False,
            "rest": False,
            "jan": False,
            "rent": True,
            "beer": True,
            "jam": True,
        }

        for test_word, expected in tests.items():
            self.assertEqual(expected, self.t.starts_with(test_word))
