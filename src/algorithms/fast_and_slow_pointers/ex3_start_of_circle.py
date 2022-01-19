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


def find_circle_start(_head):
    slow, fast = _head, _head
    length = 0

    while fast and fast._next:
        fast = fast._next._next
        slow = slow._next

        if fast == slow:
            length = culculate_length(slow)
            break

    pointer1, pointer2 = head, head
    for i in range(length):
        pointer2 = pointer2.next

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


def culculate_length(slow):
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
print('LinkedList cycle start: ', find_circle_start(head).value)

head.next.next.next.next.next.next = head.next.next.next
print('LinkedList cycle start: ', find_circle_start(head).value)

head.next.next.next.next.next.next = head
print('LinkedList cycle start: ', find_circle_start(head).value)
