class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        current = self
        while current.next:
            print(current.value, end=' -> ')
            current = current.next
        print(current.value)
        print()


def reverse(head):
    current = head
    prev = None

    while current:
        _next = current.next
        current.next = prev

        prev = current
        current = _next

    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

reverse(head).print_list()
