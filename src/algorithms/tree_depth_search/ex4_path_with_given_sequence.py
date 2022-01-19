import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def find_path(root, sequence):
    all_paths = []
    find_path_recursive(root, all_paths, [], sequence)
    return bool(all_paths)


def find_path_recursive(root, all_paths, path, sequence):
    if not root:
        return

    path.append(root.val)

    if not root.left and not root.right:
        if path == sequence:
            all_paths.append(list(path))
            return
    else:
        find_path_recursive(root.left, all_paths, path, sequence)
        find_path_recursive(root.right, all_paths, path, sequence)

    del path[-1]


root = TreeNode(1)

root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(1)

root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print(find_path(root, [1, 0, 1]))
print(find_path(root, [1, 1, 6]))
print(find_path(root, [1, 1, 5]))
print(find_path(root, [1, 1, 1]))
