# way 1:
import collections
import functools
from typing import List


def group_by(numbers: List, key_func=lambda _: _):
    res = collections.defaultdict(list)
    for item in numbers:
        res[key_func(item)] += [item]
    return res


def mod3(n): return n % 3


numbers = [1, 4, 5, 6, 8, 19, 34, 55]
print(group_by(numbers, key_func=mod3))

numbers = [1, 4, 1, 6, 3, 19, 34, 3]
print(group_by(numbers))


# way 2:
def group_by(numbers, key_func=lambda _: _):
    accumulator = lambda aggr, item: aggr[key_func(item)].append(item) or aggr
    return functools.reduce(accumulator, numbers, collections.defaultdict(list))


def mod3(n): return n % 3


numbers = [1, 4, 5, 6, 8, 19, 34, 55]
print(group_by(numbers, key_func=mod3))


numbers = [1, 4, 1, 6, 3, 19, 34, 3]
print(group_by(numbers))
