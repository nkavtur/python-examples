class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, ' -> ', end='')
            temp = temp.next
        print(None)


def is_palindrome(_head):
    middle = find_middle(_head)
    second_half = reverse(middle)
    copy_second_half = second_half

    res = True

    while second_half and _head:
        if _head.value != second_half.value:
            res = False
            break
        _head = _head.next
        second_half = second_half.next

    reverse(copy_second_half)
    return res


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
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)
print('Is Palindrome: ', is_palindrome(head))
head.print_list()

head.next.next.next.next.next = Node(2)
print('\nIs Palindrome: ', is_palindrome(head))
head.print_list()
