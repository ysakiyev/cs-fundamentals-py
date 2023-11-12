from unittest import TestCase, main
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.ll = LinkedList(0)

    def test_get_vals(self):
        self.setUp()
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)

        vals = self.ll.get_vals()
        self.assertListEqual(vals, [0, 10, 20, 30, 40, 50, 60])

    def test_append(self):
        self.setUp()
        self.ll.append(10)
        self.ll.append(20)

        self.assertEqual(self.ll.len, 3)
        self.assertEqual([0, 10, 20], self.ll.get_vals())

    def test_prepend(self):
        self.setUp()
        self.ll.prepend(10)

        self.assertEqual(self.ll.len, 2)
        self.assertEqual(self.ll.head.val, 10)
        self.assertEqual([10, 0], self.ll.get_vals())

        self.ll.prepend(20)
        self.assertEqual(self.ll.len, 3)
        self.assertEqual(self.ll.head.val, 20)
        self.assertEqual([20, 10, 0], self.ll.get_vals())

    def test_insert(self):
        self.setUp()

        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)

        self.ll.insert(5, 0)
        self.assertEqual(self.ll.len, 8)
        self.assertEqual([5, 0, 10, 20, 30, 40, 50, 60], self.ll.get_vals())

        self.ll.insert(6, 3)
        self.assertEqual(self.ll.len, 9)
        self.assertEqual([5, 0, 10, 6, 20, 30, 40, 50, 60], self.ll.get_vals())

    def test_delete(self):
        self.setUp()
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)

        self.ll.delete(30)
        self.assertEqual(self.ll.len, 6)
        self.assertEqual([0, 10, 20, 40, 50, 60], self.ll.get_vals())

    def test_delete_at(self):
        self.setUp()

        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)

        self.ll.delete_at(4)
        self.assertEqual(self.ll.len, 6)
        self.assertEqual([0, 10, 20, 30, 50, 60], self.ll.get_vals())

    def test_get(self):
        self.setUp()

        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)

        res = self.ll.get(4)
        self.assertEqual(res, 40)

        res = self.ll.get(5)
        self.assertEqual(res, 50)

    def test_length(self):
        self.setUp()

        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)
        self.ll.prepend(5)
        self.ll.delete(20)
        self.ll.delete_at(4)

        self.assertEqual(self.ll.len, 6)

    def test_reverse(self):
        self.setUp()

        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)
        self.ll.append(50)
        self.ll.append(60)

        self.ll.reverse()

        self.assertEqual([60, 50, 40, 30, 20, 10, 0], self.ll.get_vals())


if __name__ == '__main__':
    main()
