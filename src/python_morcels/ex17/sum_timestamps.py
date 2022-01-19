from typing import List


# solution + bonus 1
def sum_timestamps(timestamps: List[str]):
    def to_seconds(timestamp):
        mm, ss = timestamp.split(':')
        return int(mm) * 60 + int(ss)

    seconds = (
        to_seconds(timestamp)
        for timestamp in timestamps
    )

    mm, ss = divmod(sum(seconds), 60)
    hh, mm = divmod(mm, 60)

    if hh:
        return f"{hh}:{mm:02d}:{ss:02d}"
    else:
        return f"{mm}:{ss:02d}"


assert sum_timestamps(['5:32', '4:48']) == '10:20'
assert sum_timestamps(['03:10', '01:00']) == '4:10'
assert sum_timestamps(['2:10', '1:59']) == '4:09'
assert sum_timestamps(['15:32', '45:48']) == '1:01:20'

# solution + bonus 1, bonus 2

import re

regex = re.compile(
    r'''
    ^(
        (?P<hh>\d{1,2})    # hours 
    :)?
    (?P<mm>\d{1,2})   # minutes
    :
    (?P<ss>\d{1,2})$  # seconds
    ''', re.VERBOSE)


def sum_timestamps(timestamps: List[str]):
    def to_seconds(timestamp):
        group_dict = regex.match(timestamp).groupdict()
        hh, mm, ss = group_dict.pop('hh'), group_dict.pop('mm'), group_dict.pop('ss')
        return int(hh or 0) * 3600 + int(mm) * 60 + int(ss)

    seconds = (
        to_seconds(timestamp)
        for timestamp in timestamps
    )

    mm, ss = divmod(sum(seconds), 60)
    hh, mm = divmod(mm, 60)

    if hh:
        return f"{hh}:{mm:02d}:{ss:02d}"
    else:
        return f"{mm:01d}:{ss:02d}"


assert sum_timestamps(['5:32', '4:48']) == '10:20'
assert sum_timestamps(['03:10', '01:00']) == '4:10'
assert sum_timestamps(['2:10', '1:59']) == '4:09'
assert sum_timestamps(['15:32', '45:48']) == '1:01:20'
assert sum_timestamps(['6:15:32', '2:45:48']) == '9:01:20'
assert sum_timestamps(['6:35:32', '2:45:48', '40:10']) == '10:01:30'

print(sum_timestamps(['1:02:01', '40:01:05', '10:57:30']))
