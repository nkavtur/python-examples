import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def __repr__(self):
        return f"TreeNode(val={self.val})"

    def prent_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + '->', end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next

            print('None', end='')
            print()


def connect_level_order_siblings(root):
    queue = collections.deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.popleft()

            if i < level_size - 1:
                next = queue.popleft()
                current.next = next
                queue.appendleft(next)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return root


root = TreeNode(12)

root.left = TreeNode(7)
root.right = TreeNode(1)

root.left.left = TreeNode(9)

root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

connect_level_order_siblings(root)
root.prent_level_order()
