from typing import List, Iterable


# solution way1, bonus1
def numeric_range(numbers: List[int]):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1] - sorted_numbers[0]


assert numeric_range([10, 8, 7, 5, 3, 6, 2]) == 8
assert numeric_range([1, 2, 3]) == 2
assert numeric_range([4]) == 0
assert numeric_range([]) == 0


# solution way1, bonus1, bonus2
def numeric_range(numbers: Iterable[int]):
    try:
        _iter = iter(numbers)
        first = next(_iter)
        _max, _min = first, first

        for number in numbers:
            if number >= _max:
                _max = number
            if number <= _min:
                _min = number

        return _max - _min
    except StopIteration:
        return 0


assert numeric_range([10, 8, 7, 5, 3, 6, 2]) == 8
assert numeric_range([1, 2, 3]) == 2
assert numeric_range([4]) == 0
assert numeric_range([]) == 0
assert numeric_range({4, 2, 7, 3, 8}) == 6
assert numeric_range(n ** 2 for n in range(10)) == 81
assert numeric_range(n for n in []) == 0

# solution way2, bonus1, bonus2
from functools import reduce


def min_max(accumulator, value):
    current_min, current_max = accumulator
    return min(current_min, value), max(current_max, value)


def numeric_range(numbers: Iterable[int]):
    _iter = iter(numbers)
    try:
        first = next(_iter)
    except StopIteration:
        return 0

    smallest, biggest = reduce(min_max, numbers, (first, first))
    return biggest - smallest


assert numeric_range([10, 8, 7, 5, 3, 6, 2]) == 8
assert numeric_range([1, 2, 3]) == 2
assert numeric_range([4]) == 0
assert numeric_range([]) == 0
assert numeric_range({4, 2, 7, 3, 8}) == 6
assert numeric_range(n ** 2 for n in range(10)) == 81
assert numeric_range(n for n in []) == 0
