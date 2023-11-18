from unittest import TestCase
from heap import Heap


class TestHeap(TestCase):
    def setUp(self):
        self.heap = Heap()
        self.heap.data = [0, 14, 19, 16, 21, 26, 19, 68, 65, 30]

    def test_push(self):
        self.heap.push(17)
        self.assertListEqual([0, 14, 17, 16, 21, 19, 19, 68, 65, 30, 26], self.heap.data)

    def test_pop(self):
        res = self.heap.pop()
        self.assertEqual(res, 14)
        self.assertListEqual([0, 16, 19, 19, 21, 26, 30, 68, 65], self.heap.data)
