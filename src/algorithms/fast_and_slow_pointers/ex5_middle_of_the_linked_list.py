class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()


def find_middle(_head):
    slow, fast = _head, _head
    length = 0

    while fast and fast._next:
        fast = fast._next._next
        slow = slow._next

    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print('Middle of the linked list: ', find_middle(head).value)

head.next.next.next.next.next = Node(6)
print('Middle of the linked list: ', find_middle(head).value)

head.next.next.next.next.next = Node(7)
print('Middle of the linked list: ', find_middle(head).value)
