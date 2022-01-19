import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def level_averages(root):
    result = []

    queue = collections.deque([root])
    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)
root.left.right = TreeNode(2)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("level averages: " + str(level_averages(root)))
