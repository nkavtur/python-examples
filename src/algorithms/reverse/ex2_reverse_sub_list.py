class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        current = self
        guard = 0
        while current.next and guard < 10:
            print(current.value, end=' -> ')
            current = current.next
            guard += 1
        print(current.value)
        print()


def reverse_sub_list(head, p, q):
    current, prev, i = head, None, 1
    while current and i < p:
        prev = current
        current = current.next
        i += 1
    start, pre_start = current, prev

    prev, current, i = start, start.next, i + 1
    start.next = None
    while current and i <= q:
        _next = current.next
        current.next = prev
        prev = current
        current = _next
        i += 1

    if pre_start:
        pre_start.next = prev
    else:
        head = prev
    start.next = current
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.print_list()
reverse_sub_list(head, 1, 4).print_list()

