# way1 + bonus1
def tail(sequence, n):
    pos = len(sequence) - n if n < len(sequence) else 0
    return list(sequence[pos:])


assert tail([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert tail('hello', 2) == ['l', 'o']
assert tail('hello', 0) == []


# way2 + bonus1
def tail(sequence, n):
    if n <= 0:
        return []
    return list(sequence[-n:])


assert tail([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert tail('hello', 2) == ['l', 'o']
assert tail('hello', 0) == []


# bonus2, way1:
def tail(iterable, n):
    if n <= 0:
        return []

    items = []
    for item in iterable:
        if n == 1:
            items = [item]
        else:
            items = [*items[-(n - 1):], item]

    return items


squares = (n ** 2 for n in range(10))
assert tail(squares, 3) == [49, 64, 81]


# bonus2, way2:
def tail(iterable, n):
    if n <= 0:
        return []

    if n == 1:
        index = slice(0, 0)
    else:
        index = slice(-(n - 1), None)

    items = []
    for item in iterable:
        items = [*items[index], item]

    return items


squares = (n ** 2 for n in range(10))
assert tail(squares, 3) == [49, 64, 81]

# bonus2, way3:
from collections import deque


def tail(iterable, n):
    if n <= 0:
        return []

    queue = deque([], n)

    for item in iterable:
        queue.append(item)

    return list(queue)


squares = (n ** 2 for n in range(10))
assert tail(squares, 3) == [49, 64, 81]


# bonus2, way4:
def tail(iterable, n):
    if n <= 0:
        return []

    return list(deque(iterable, maxlen=n))  # works exactly same way as above one


squares = (n ** 2 for n in range(10))
assert tail(squares, 3) == [49, 64, 81]


array = [1, 2, 3, 4, 5]
index = slice(1, None)
print(array[index])
