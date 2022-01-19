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


def connect_all_level_order_siblings(root):
    queue = collections.deque([root])

    prev_node = None
    while queue:
        current_node = queue.popleft()

        if prev_node:
            prev_node.next = current_node
        prev_node = current_node

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return root


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

connect_all_level_order_siblings(root)
root.print_tree()
