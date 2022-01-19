from collections.abc import Iterable, Sequence


# solution way1:
def compact(sequence: Sequence):
    res = []
    for index, item in enumerate(sequence):
        if index == 0 or item != sequence[index - 1]:
            res.append(item)
    return res


assert compact([1, 1, 1]) == [1]
assert compact([1, 1, 2, 2, 3, 2]) == [1, 2, 3, 2]
assert compact([]) == []


# solution way2:
def compact(sequence: Sequence):
    res = []
    for current, previous in zip(sequence, [object(), *sequence]):
        if current != previous:
            res.append(current)

    return res


assert compact([1, 1, 1]) == [1]
assert compact([1, 1, 2, 2, 3, 2]) == [1, 2, 3, 2]
assert compact([]) == []


# solution + bonus1 way1
def compact(iterable: Iterable):
    if not iterable:
        return []

    iterator = iter(iterable)
    previous = next(iterator)
    res = [previous]

    for item in iterator:
        if item != previous:
            res.append(item)
            previous = item

    return res


assert compact([1, 1, 1]) == [1]
assert compact([1, 1, 2, 2, 3, 2]) == [1, 2, 3, 2]
assert compact([]) == []
assert compact(n ** 2 for n in [1, 2, 2]) == [1, 4]


# solution + bonus1 way2
def compact(iterable: Iterable):
    previous = object()
    res = []

    for item in iterable:
        if item != previous:
            res.append(item)
            previous = item

    return res


assert compact([1, 1, 1]) == [1]
assert compact([1, 1, 2, 2, 3, 2]) == [1, 2, 3, 2]
assert compact([]) == []
assert compact(n ** 2 for n in [1, 2, 2]) == [1, 4]


# solution + bonus1 + bonus 2 wqy1
def compact(iterable: Iterable):
    previous = object()
    for item in iterable:
        if item != previous:
            yield item
            previous = item


c = compact(n ** 2 for n in [1, 2, 2])
assert iter(c) is c
assert list(compact([1, 1, 1])) == [1]
assert list(compact([1, 1, 2, 2, 3, 2])) == [1, 2, 3, 2]
assert list(compact([])) == []
assert list(compact(n ** 2 for n in [1, 2, 2])) == [1, 4]

# solution + bonus1 + bonus 2 way2
from itertools import groupby


def compact(iterable: Iterable):
    return (
        item
        for item, group in groupby(iterable)
    )


c = compact(n ** 2 for n in [1, 2, 2])
assert iter(c) is c
assert list(compact([1, 1, 1])) == [1]
assert list(compact([1, 1, 2, 2, 3, 2])) == [1, 2, 3, 2]
assert list(compact([])) == []
assert list(compact(n ** 2 for n in [1, 2, 2])) == [1, 4]
