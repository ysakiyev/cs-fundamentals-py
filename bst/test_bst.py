from unittest import TestCase
from bst import Bst


class TestBst(TestCase):
    def setUp(self):
        self.bst = Bst(5)

    def test_insert(self):
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)
        self.bst.insert(10)

    def test_search(self):
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)
        self.bst.insert(10)

        self.assertEqual(True, self.bst.search(3))
        self.assertEqual(True, self.bst.search(4))
        self.assertEqual(True, self.bst.search(5))
        self.assertEqual(True, self.bst.search(6))
        self.assertEqual(False, self.bst.search(7))
        self.assertEqual(True, self.bst.search(8))
        self.assertEqual(True, self.bst.search(9))
        self.assertEqual(True, self.bst.search(10))
        self.assertEqual(False, self.bst.search(11))

    def test_remove(self):
        # TODO: make test more comprehensive
        self.bst.root.val = 4
        self.bst.insert(3)
        self.bst.insert(2)
        self.bst.insert(6)
        self.bst.insert(5)
        self.bst.insert(7)

        self.bst.remove(4)
        self.assertEqual(False, self.bst.search(4))
