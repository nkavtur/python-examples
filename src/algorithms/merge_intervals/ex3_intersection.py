class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def intersection(intervals_a, intervals_b):
    merged = []
    start, end = 0, 1

    i, j = 0, 0

    while i < len(intervals_a) and j < len(intervals_b):
        a_overlaps_b = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]
        b_overlaps_a = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        if a_overlaps_b or b_overlaps_a:
            merged.append([
                max(intervals_a[i][start], intervals_b[j][start]),
                min(intervals_a[i][end], intervals_b[j][end])
            ])

        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return merged


def is_intersection(interval1, interval2):
    start, end = 0, 1
    return interval1[end] >= interval2[start]


print(intersection(
    [[1, 3], [5, 6], [7, 9]],
    [[2, 3], [5, 7]])
)
# Output: [2, 3], [5, 6], [7, 7]

print(intersection(
    [[1, 3], [4, 7], [9, 12]],
    [[5, 10]])
)
# Output: [5, 7], [9, 10]
