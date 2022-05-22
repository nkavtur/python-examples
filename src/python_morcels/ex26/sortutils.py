import re
from functools import singledispatch

convert = lambda text: int(text) if text.isdigit() else text.lower()


@singledispatch
def natural_key(thing):
    raise TypeError(f"Unknown type: {type(thing)}")


@natural_key.register(str)
def _string_key(string):
    return [convert(part) for part in re.split('\s+', string)]


def natural_sort(iterable, key=natural_key, reverse=False):
    return sorted(iterable, key=key, reverse=reverse)
