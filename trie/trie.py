class TrieNode:
    def __init__(self, ch):
        self.char = ch
        self.children = {}
        self.is_complete = False


# Prefix tree
class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    # insert the string into the trie
    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                new_node = TrieNode(c)
                cur.children[c] = new_node
            cur = cur.children[c]

        cur.is_complete = True

    # returns True if the string word is in the trie(i.e., was inserted before)
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.is_complete

    # returns True if there is a previously inserted string that has the prefix
    def starts_with(self, prefix) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
