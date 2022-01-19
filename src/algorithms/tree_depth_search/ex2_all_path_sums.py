import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def find_paths(root, s):
    all_paths = []
    find_paths_recursive(root, s, [], all_paths)
    return all_paths


def find_paths_recursive(root, s, path, all_paths):
    if not root:
        return

    path.append(root.val)

    if root.val == s and not root.left and not root.right:
        all_paths.append(list(path))
    else:
        find_paths_recursive(root.left, s - root.val, path, all_paths)
        find_paths_recursive(root.right, s - root.val, path, all_paths)

    # del path[-1]1


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(4)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(find_paths(root, 23))
