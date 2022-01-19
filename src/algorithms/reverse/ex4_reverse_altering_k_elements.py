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


def reverse_altering_k_elements(head, k):
    i = 1
    temp_head = reverse_sublist(head, 1, k)

    i += 2 * k
    while reverse_sublist(temp_head, i, i + k - 1):
        i += k * 2

    return temp_head


def reverse_sublist(head, p, q):
    current, prev, i = head, None, 1
    while current and i < p:
        prev = current
        current = current.next
        i += 1

    last_node_of_first_half = prev
    first_node_of_sublist = current

    if not current:
        return None

    prev, current = current, current.next
    while current and i < q:
        _next = current.next
        current.next = prev
        prev = current
        current = _next
        i += 1

    first_node_of_sublist.next = current
    if last_node_of_first_half:
        last_node_of_first_half.next = prev
    else:
        return prev

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)

reverse_altering_k_elements(head, 2).print_list()

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
