class Node:

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        next_value = self.next.key if self.next else None
        prev_value = self.prev.key if self.prev else None
        return f"Node(key={self.key}, next={next_value}, prev={prev_value})"


class LinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def delete(self, node):
        if node == self.head:
            self.pop_left()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

        node.next = node.prev = None

    def pop_left(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

        return temp

    def append(self, node):
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def __len__(self):
        return self.size

    def print_list(self):
        node = self.head
        while node.next:
            print(node, '->', end=' ')
            node = node.next
        print(node)


class LRUCache:

    def __init__(self, capacity):
        self.linked_list = LinkedList()
        self.internal_cache = dict()
        self.capacity = capacity

    def put(self, k, v):
        if k in self.internal_cache:
            self.linked_list.delete(self.internal_cache[k])

        node = Node(k, v)
        self.linked_list.append(node)
        self.internal_cache[k] = node

        if len(self.linked_list) > self.capacity:
            deleted = self.linked_list.pop_left()
            del self.internal_cache[deleted.key]

    def get(self, k):
        if k not in self.internal_cache:
            return None

        node = self.internal_cache[k]
        self.linked_list.delete(node)
        self.linked_list.append(node)

    def __repr__(self):
        _str = ''
        for i, (k, v) in enumerate(self.internal_cache.items()):
            _str += f"{k.__repr__()}: {v.value.__repr__()}"
            if i != len(self.internal_cache) - 1:
                _str += ', '
        return "{" + _str + "}"


lru_cache = LRUCache(4)

lru_cache.put(1, "one")
lru_cache.put(2, "two")
lru_cache.put(3, "three")
lru_cache.put(4, "four")
print(lru_cache)
lru_cache.linked_list.print_list()

print()
lru_cache.get(1)
print(lru_cache)
lru_cache.linked_list.print_list()

print()
lru_cache.put(5, "five")
print(lru_cache)
lru_cache.linked_list.print_list()

#
# lru_cache.insert(5, "five")
# print(lru_cache)
