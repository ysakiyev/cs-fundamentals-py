class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = node

        self.len = 1

    def append(self, val: int):
        self.tail.next = Node(val)
        self.tail = self.tail.next

        self.len += 1

    def prepend(self, val: int):
        node = Node(val)
        node.next = self.head
        self.head = node

        self.len += 1

    def insert(self, val: int, index: int):
        if index >= self.len:
            return

        prev = None
        cur = self.head
        i = 0

        while i < index:
            prev = cur
            cur = cur.next
            i += 1

        node = Node(val)
        if prev is not None:
            prev.next = node

        node.next = cur
        if cur is self.head:
            self.head = node

        self.len += 1

    def delete(self, val: int):
        prev = None
        cur = self.head

        while cur.val != val:
            prev = cur
            cur = cur.next

        if cur.val == val:
            prev.next = cur.next
            self.len -= 1

    def delete_at(self, index: int):
        if index >= self.len:
            return

        prev = None
        cur = self.head
        i = 0

        while i < index:
            prev = cur
            cur = cur.next
            i += 1

        prev.next = cur.next
        self.len -= 1

    def get(self, index: int):
        if index < 0 or index >= self.len:
            return

        cur = self.head
        i = 0

        while i < index:
            cur = cur.next
            i += 1

        return cur.val

    def length(self):
        return self.len

    def reverse(self):
        cur = self.head
        prev = None

        while cur is not None:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt

        self.head = prev

    def get_vals(self):
        cur = self.head
        vals = []

        while cur is not None:
            vals.append(cur.val)
            cur = cur.next

        return vals
