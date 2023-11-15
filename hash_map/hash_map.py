class Node:
    key: str
    val: str

    def __init__(self, key, val: str):
        self.key = key
        self.val = val
        self.next = None


class LLBucket:
    head: Node | None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def upsert(self, node: Node):
        if self.head is None:
            self.head = node
            return

        cur = self.head

        while cur is not None:
            if cur.key == node.key:
                cur.val = node.val

            if cur.next is None:
                cur.next = node
                self.size += 1
            cur = cur.next

    def search_key(self, key: str):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return None

    def remove(self, key: str):
        cur = self.head
        prev = None

        while cur is not None:
            nextt = cur.next
            if cur.key == key:
                cur.next = None
                if prev is not None:
                    prev.next = nextt
                self.head = nextt
                return True
            prev = cur
            cur = cur.next

        return False


HM_NUM_BUCKETS = 16


class HashMap:
    def __init__(self):
        self.buckets = [LLBucket() for _ in range(HM_NUM_BUCKETS)]

    def get_index(self, key: object):
        return key.__hash__() % HM_NUM_BUCKETS

    def set(self, key: str, val: str):
        node = Node(key, val)
        idx = self.get_index(key)
        self.buckets[idx].upsert(node)

    def get(self, key: str) -> str:
        idx = self.get_index(key)
        return self.buckets[idx].search_key(key)

    def rm(self, key: str):
        idx = self.get_index(key)
        self.buckets[idx].remove(key)

