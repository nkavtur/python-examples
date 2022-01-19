def maxEvents(arrival, duration):
    intervals = []

    for i in range(len(arrival)):
        intervals.append([arrival[i], arrival[i] + duration[i]])

    start, end = 0, 1

    intersections_count = 0
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):

            interval_a = intervals[i]
            interval_b = intervals[j]

            a_overlaps_b = interval_a[start] <= interval_b[end] <= interval_a[end]
            b_overlaps_a = interval_b[start] <= interval_a[end] <= interval_b[end]
            if (a_overlaps_b or b_overlaps_a) \
                    and not (interval_a[start] < interval_b[start] and interval_a[end] == interval_b[start]) \
                    and not (interval_b[start] < interval_a[start] and interval_b[end] == interval_a[start]):
                intersections_count += 1

    return 1 + intersections_count


print(
    maxEvents([1, 1, 2, 5, 7], [3, 1, 2, 2, 1])
)
