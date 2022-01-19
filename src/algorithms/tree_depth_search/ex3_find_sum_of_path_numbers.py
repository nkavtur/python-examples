import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def find_sum_of_path_numbers(root):
    return sum_of_paths_recursive(root, 0)


def sum_of_paths_recursive(root, s):
    if not root:
        return 0

    s = s * 10 + root.val

    if not root.left and not root.right:
        return s
    else:
        return sum_of_paths_recursive(root.left, s) + sum_of_paths_recursive(root.right, s)


root = TreeNode(1)

root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(1)

root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print(find_sum_of_path_numbers(root))
