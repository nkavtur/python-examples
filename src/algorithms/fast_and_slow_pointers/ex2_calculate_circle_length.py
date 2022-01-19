class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def calculate_length(_head):
    slow, fast = _head, _head

    while fast and fast._next:
        fast = fast._next._next
        slow = slow._next

        if fast == slow:
            return _calculate_length(slow)

    return False


def _calculate_length(slow):
    current = slow
    length = 0

    while True:
        current = current._next
        length += 1

        if current == slow:
            return length


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print('LinkedList has cycle: ', calculate_length(head))

head.next.next.next.next.next.next = head.next.next.next
print('LinkedList has cycle: ', calculate_length(head))
