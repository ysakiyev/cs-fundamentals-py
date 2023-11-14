class Node:
    def __init__(self, key, val: object):
        self.key = key
        self.val = val
        self.next = None


class LLBucket:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node: Node):
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
        self.size += 1

    def search(self, key: object):
        return

    def remove(self, key: object):
        return


class HashMap:
    def __init__(self):
        self.size = 16
        self.buckets = [LLBucket() for _ in range(16)]

    def get_index(self, key: object):
        return key.__hash__() % self.size

    def set(self, key: object, val: object):
        node = Node(key, val)
        idx = self.get_index(key)
        self.buckets[idx].append(node)

    def get(self, key: object) -> object:
        idx = self.get_index(key)
        return self.buckets[idx].search(key)

    def rm(self, key: object):
        idx = self.get_index(key)
        self.buckets[idx].remove(key)

    def size(self) -> int:
        return self.size

