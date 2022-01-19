class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def insert_and_merge(intervals, new_interval):
    res = []

    i = 0
    while new_interval.start > intervals[i].end:
        res.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i].start <= new_interval.end:
        start = min(new_interval.start, intervals[i].start)
        end = max(new_interval.end, intervals[i].end)
        new_interval = Interval(start, end)
        i += 1
    res.append(new_interval)

    while i < len(intervals):
        res.append(intervals[i])
        i += 1

    return res


intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
print(insert_and_merge(intervals, Interval(4, 6)))
# Output: [[1,3], [4,7], [8,12]]

intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
print(insert_and_merge(intervals, Interval(4, 10)))
# Output: [[1,3], [4,12]]

intervals = [Interval(2, 3), Interval(5, 7)]
print(insert_and_merge(intervals, Interval(1, 4)))
# Output: [[1,4], [5,7]]
