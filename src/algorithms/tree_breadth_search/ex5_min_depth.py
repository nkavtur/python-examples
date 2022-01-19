import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def min_depth(root):
    level_index = 1

    queue = collections.deque([root])
    while queue:
        level_size = len(queue)

        for _ in range(level_size):

            node = queue.popleft()

            if not node.left and not node.right:
                return level_index

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        level_index += 1
    return level_index



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

root.right.right.left = TreeNode(11)

print("min depth: " + str(min_depth(root)))
