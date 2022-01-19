import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"


def find_successor(root, key):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        if node.val == key:
            break

    return queue[0] if queue else None


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

root.right.right.left = TreeNode(11)

print("node successor: " + str(find_successor(root, 7)))
