import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def traverse(root):
    result = []

    queue = collections.deque(iterable=[root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print('queue: ', queue, ', level_size:', level_size, ', node:', node, ', level:', level)

        result.append(level)

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("level order traversal: " + str(traverse(root)))
