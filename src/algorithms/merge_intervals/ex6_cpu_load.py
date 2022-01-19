from heapq import *


def min_meeting_rooms(meetings):
    start, end = 0, 1
    meetings = sorted(meetings, key=lambda m: m[start])

    heap = []
    min_rooms = 0

    for i in range(0, len(meetings)):
        print(heap)
        while len(heap) > 0 and heap[0][end] <= meetings[i][start]:
            heappop(heap)

        heappush(heap, meetings[i])
        min_rooms = max(min_rooms, len(heap))
    return min_rooms


# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
# occur in any of the two rooms later.
# print(min_meeting_rooms([[1, 4], [2, 5], [7, 9]]))

# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
# print(min_meeting_rooms([[6, 7], [2, 4], [8, 12]]))

# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
# hold all the meetings.
# print(min_meeting_rooms([[1, 4], [2, 3], [3, 6]]))

# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
print(min_meeting_rooms([[4, 5], [2, 3], [3, 4], [2, 4], [3, 5]]))
