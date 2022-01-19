# way1:
def with_previous1(sequence):
    res = []
    for index, item in enumerate(sequence):
        previous = sequence[index - 1] if index != 0 else None
        res.append((item, previous))

    return res


# way2:
def with_previous2(sequence):
    previous = [
        sequence[index - 1] if index != 0 else None
        for index in range(len(sequence))
    ]

    return zip(sequence, previous)


print(list(with_previous2("hello")))
print(list(with_previous2([1, 2, 3])))


# way3:
def with_previous3(sequence):
    return zip(sequence, [None, *sequence])


print(list(with_previous3("hello")))
print(list(with_previous3([1, 2, 3])))


# bonus1, way1:
def with_previous4(iterable):
    sequence = list(iterable)
    return zip(sequence, [None, *sequence])


# bonus1, way2:
def with_previous5(iterable):
    """Provide each iterable item with item before it."""
    previous = None
    items = []
    for item in iterable:
        items.append((item, previous))
        previous = item
    return items


# bonus2, way1: NEVER implement your own iterator!!!!
class WithPrevious:

    def __init__(self, *, iterable):
        self.iterator = iter(iterable)
        self.next = None
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        self.current, self.next = self.next, next(self.iterator)
        return self.next, self.current


def with_previous6(iterable):
    return list(WithPrevious(iterable=iterable))


# bonus2, way2: USE generator functions instead!!!
def with_previous7(iterable):
    """Provide each iterable item with item before it."""
    previous = None
    for item in iterable:
        yield item, previous
        previous = item


# bonus2, way2:
from itertools import tee, chain


def with_previous9(iterable):
    """Provide each iterable item with item before it."""
    i1, i2 = tee(iterable)
    return zip(i1, chain([None], i2))


print(list(with_previous9("hello")))
print(list(with_previous9([1, 2, 3])))
