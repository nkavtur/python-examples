class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        i = 0
        while temp is not None and i < 10:
            print(temp.value, ' -> ', end='')
            i += 1
            temp = temp.next
        print(None)


def reorder(_head):
    middle = find_middle(_head)
    second_half = reverse(middle)
    copy_head = _head

    while second_half != middle:
        _next1 = _head.next
        _next2 = second_half.next

        _head.next = second_half
        second_half.next = _next1

        _head = _next1
        second_half = _next2

    _head = copy_head


def find_middle(_head):
    slow, fast = _head, _head
    while fast and fast._next:
        fast = fast._next._next
        slow = slow._next
    return slow


def reverse(_head):
    prev = None
    while _head:
        _next = _head.next
        _head.next = prev
        prev = _head
        _head = _next
    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
reorder(head)
head.print_list()

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
reorder(head)
head.print_list()
