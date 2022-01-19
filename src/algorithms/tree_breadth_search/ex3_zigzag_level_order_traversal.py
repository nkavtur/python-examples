import collections
from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def zigzag_traverse(root):
    result = []

    queue, level_index = deque([root]), 1
    while queue:
        level_size = len(queue)
        level = deque()
        for _ in range(level_size):
            node = queue.popleft()

            if level_index % 2 == 0:
                level.appendleft(node.val)
            else:
                level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level_index += 1
        result.append(level)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)

print("zigzag traversal: " + str(zigzag_traverse(root)))
