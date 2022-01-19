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


def rotate(head, k):
    size = calculate_size(head)
    k = k if k < size else k // size + 1

    current, prev, i = head, None, 1
    while current and i <= k:
        prev = current
        current = current.next
        i += 1

    new_head, new_end = current, prev
    while current:
        prev = current
        current = current.next

    prev.next = head
    new_end.next = None
    return new_head


def calculate_size(head):
    i, current = 1, head
    while current.next:
        current = current.next
        i += 1
    return i


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

rotate(head, 8).print_list()



# head.next.next.next.next.next = Node(6)
# temp_head = reverse_sublist(head, 1, 2)
# temp_head.print_list()
#
# reverse_sublist(temp_head, 5, 6)
# temp_head.print_list()
#
# reverse_sublist(temp_head, 9, 10)
# temp_head.print_list()
#
# reverse_sublist(temp_head, 13, 14)
# temp_head.print_list()
