# way1:
def uniques_only(iterables):
    res = []

    for index, item in enumerate(iterables):
        if item not in iterables[index:]:
            res.append(item)

    return res


# way2:
def uniques_only2(iterable):
    seen, res = set(), []

    for item in iterable:
        if item not in seen:
            res.append(item)
        seen.add(item)

    return res


# way3:
def uniques_only3(iterable):
    def seen(item, counts=set()):
        seen = item in counts
        counts.add(item)
        return seen

    return [
        item for item in iterable
        if not seen(item)
    ]


# way4:
def uniques_only4(iterable):
    seen = set()
    seen_add = seen.add
    return [
        item for item in iterable
        if not (item in seen or seen_add(item))
    ]


# way5: dictionaries retain order, but sets don't
def uniques_only5(iterable):
    return list(dict.fromkeys(iterable))


# bonus1:
def uniques_only6(iterable):
    seen = set()
    seen_add = seen.add
    return (
        item for item in iterable
        if not (item in seen or seen_add(item))
    )


# bonus2:
def uniques_only7(iterable):
    seen = []
    seen_add = seen.append
    return (
        item for item in iterable
        if not (item in seen or seen_add(item))
    )


# bonus 3, way1:
from collections.abc import Hashable


def uniques_only(iterable):
    def seen(i, nonhashable_seen=[], hashable_seen=set()):
        if isinstance(i, Hashable):
            _seen, _seen_add = hashable_seen, hashable_seen.add
        else:
            _seen, _seen_add = nonhashable_seen, nonhashable_seen.append

        return i in _seen or _seen_add(i)

    return (
        i for i in iterable
        if not seen(i)
    )


print(list(uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']])))
print(list(uniques_only([1, 2, 2, 1, 1, 3, 2, 1])))

print(isinstance([1, 2, 2, 1, 1, 3, 2, 1], Hashable))
