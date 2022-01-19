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
        # print()


def reverse_every_k_elements(head, k):
    i = 1
    temp_head = reverse_sublist(head, 1, k)

    i += k
    while reverse_sublist(temp_head, i, i + k - 1):
        i += k

    return temp_head


def reverse_sublist(head, p, q):
    current, prev, i = head, None, 1

    # skipping first p elements
    while current and i < p:
        prev = current
        current = current.next
        i += 1

    if not current:
        return

    first_node_of_sublist = current  # 4
    last_node_of_first_half = prev  # 6

    prev, current = current, current.next  # 4, 5
    while current and i < q:
        _next = current.next
        current.next = prev
        prev = current
        current = _next
        i += 1

    if last_node_of_first_half:
        last_node_of_first_half.next = prev
    else:
        head = prev

    first_node_of_sublist.next = current

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
# head.next.next.next.next.next.next.next.next = Node(9)

# head.print_list()
reverse_every_k_elements(head, 3).print_list()

# temp_head = reverse_sublist(head, 1, 3)
# temp_head.print_list()
# print(temp_head.value)
# print(head.value, end='\n\n')

# temp_head = reverse_sublist(temp_head, 4, 6)
# temp_head.print_list()
# print(temp_head.value)
# print(head.value, end='\n\n')

# temp_head = reverse_sublist(temp_head, 7, 9)
# temp_head.print_list()
# print(temp_head.value)
# print(head.value, end='\n\n')
