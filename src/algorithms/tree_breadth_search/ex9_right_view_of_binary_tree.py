import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"

    def print_tree(self):
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def tree_right_view(root):
    result = []
    queue = collections.deque([root])

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

        result.append(level[-1])

    return result


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

root.left.left.left = TreeNode(3)

print(tree_right_view(root))
