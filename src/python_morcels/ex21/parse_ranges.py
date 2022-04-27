# my solution 1:
import re

pattern = r'''
    \b(?P<start>\d+)
    (?P<arrow>-\>)?
    (?P<hyphen>-)?
    (?P<end>\d+)?\b
'''
REGEX = re.compile(pattern, re.VERBOSE)


def parse_ranges(s: str):
    for str_range in s.split(','):
        groups = REGEX.search(str_range).groupdict()

        start = groups['start']
        end = groups['end'] if groups['hyphen'] else start

        yield from range(int(start), int(end) + 1)


assert list(parse_ranges('1-2,4-4,8-13')) == [1, 2, 4, 8, 9, 10, 11, 12, 13]
assert list(parse_ranges('0-0, 4-8, 20-20, 43-45')) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
assert list(parse_ranges('0,4-8,20,43-45')) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
assert list(parse_ranges('0, 4-8, 20->exit, 43-45')) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]


# solution 2:
def partition(sep, group):
    """Return (start, end) tuple from given number group."""
    a, _, b = group.partition(sep)
    return ((a, b) if b.isnumeric() else (a, a))


def parse_ranges(ranges_string):
    """Return iterable based on comma-separated numeric ranges."""
    # !!!! we are using only one loop to solve it. pairs is generator and gets executed once at final step!!
    pairs = (
        partition('-', group)
        for group in ranges_string.split(',')
    )
    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop) + 1)
    )


# solution 3 without handling '->' case:
def parse_ranges(ranges_string):
    return (
        num
        for group in ranges_string.split(',')
        for a, _, b in [group.partition('-')]  # assignment in list-comprehensive !!!!!!! Cool trick!!!
        for num in range(int(a), int(b or a) + 1)
    )


# solution 4 best (with not capturing group regex trick)
PAIR_RE = re.compile(r'( \d+ )(?: - (\d+) )?', re.VERBOSE)


def parse_ranges(ranges_string):
    pairs = (
        ((a, b) if b else (a, a))
        for a, b in PAIR_RE.findall(ranges_string)
    )
    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop) + 1)
    )
