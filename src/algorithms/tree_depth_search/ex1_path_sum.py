import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def has_path(root, s):
    if not root:
        return False

    # child node
    if not root.left and not root.right:
        return root.val == s

    return has_path(root.left, s - root.val) or has_path(root.right, s - root.val)


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(4)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(has_path(root, 23))
# print(has_path(root, 16))
