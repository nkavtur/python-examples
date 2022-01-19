class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
    # print(sorted_intervals)

    merged_intervals = []
    start = sorted_intervals[0].start
    end = sorted_intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))

    return merged_intervals


intervals = [Interval(1, 3), Interval(4, 6), Interval(5, 8), Interval(8, 12)]
print(merge(intervals))
# Output: [[1, 5], [7, 9]]

intervals = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
print(merge(intervals))
# Output: [[2, 4], [5, 9]]

intervals = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
print(merge(intervals))
# Output: [[1, 6]]

