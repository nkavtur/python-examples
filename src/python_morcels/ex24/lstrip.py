import itertools


# custom implementation
def lstrip(iterable, strip_value):
    """Return iterable with strip_value items removed from beginning."""
    iterator = iter(iterable)
    if callable(strip_value):
        predicate = strip_value
    else:
        def predicate(value): return value == strip_value
    for item in iterator:
        if not predicate(item):
            yield item
            break
    yield from iterator


print(list(lstrip([], 0)))
print(list(lstrip([0, 0, 0], 0)))
# assert list(lstrip([], 0)) == [1, 0, 2, 3]
# assert list(lstrip([0, 0, 1, 0, 2, 3], 0)) == [1, 0, 2, 3]
# assert list(lstrip('  hello ', ' ')) == ['h', 'e', 'l', 'l', 'o', ' ']
#
# assert list(lstrip(['', 0, 1, 0, 2, 'h', ''], lambda n: not bool(n))) == [1, 0, 2, 'h', '']
# assert list(lstrip([-4, -2, 2, 4, -6], lambda n: n < 0)) == [2, 4, -6]
#
#
# implementation using dropwhile
# def lstrip(iterable, filter):
#     filter_fn = filter if callable(filter) else lambda val: val == filter
#     return itertools.dropwhile(filter_fn, iterable)
#
#
# print(list(lstrip([0, 0, 1, 0, 2, 3], 0)))
# assert list(lstrip([0, 0, 1, 0, 2, 3], 0)) == [1, 0, 2, 3]
# assert list(lstrip('  hello ', ' ')) == ['h', 'e', 'l', 'l', 'o', ' ']
#
# assert list(lstrip(['', 0, 1, 0, 2, 'h', ''], lambda n: not bool(n))) == [1, 0, 2, 'h', '']
# assert list(lstrip([-4, -2, 2, 4, -6], lambda n: n < 0)) == [2, 4, -6]
#
