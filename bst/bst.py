class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Bst:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        def insert_recursive(root, v):
            if v > root.val:
                if not root.right:
                    root.right = Node(v)
                else:
                    insert_recursive(root.right, v)
            else:
                if not root.left:
                    root.left = Node(v)
                else:
                    insert_recursive(root.left, v)

        insert_recursive(self.root, val)

    def search(self, val):
        def search_recursive(root, v):
            if root is None:
                return False

            if root.val == v:
                return True

            if v > root.val:
                return search_recursive(root.right, v)
            else:
                return search_recursive(root.left, v)

        return search_recursive(self.root, val)

    def find_min(self, node):
        cur = node
        while cur and cur.left:
            cur = cur.left

        return cur.val

    def remove(self, val):
        def remove_recursive(root, v):
            if root is None:
                return None

            if v > root.val:
                root.right = remove_recursive(root.right, v)
            elif v < root.val:
                root.left = remove_recursive(root.left, v)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    right_min = self.find_min(root.right)
                    root.val = right_min
                    root.right = remove_recursive(root.right, right_min)

            return root

        return remove_recursive(self.root, val)

    # def inorder(self):
    #     # Implementation for inorder traversal
    #
    # def preorder(self):
    #     # Implementation for preorder traversal
    #
    # def postorder(self):
    #     # Implementation for postorder traversal
    #