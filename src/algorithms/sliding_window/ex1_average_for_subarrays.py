array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5


# Average for sub-arrays of size k:

# Brute-force: O(n * k)
def average_for_subarrays1(array, k):
    res = []
    for i in range(0, len(array) - k + 1):
        _sum = 0
        for j in range(i, i + k):
            _sum += array[j]
        res.append(_sum / k)
    return res


assert average_for_subarrays1(array, k) == [2.2, 2.8, 2.4, 3.6, 2.8]


# Idea: O(n)
def average_for_subarrays2(array, k):
    res, _sum = [], 0
    for i in range(0, len(array) - k + 1):
        if i == 0:
            for j in range(i, i + k):
                _sum += array[j]
        else:
            _sum = _sum - array[i - 1] + array[i + k - 1]

        res.append(_sum / k)
    return res


assert average_for_subarrays1(array, k) == [2.2, 2.8, 2.4, 3.6, 2.8]


# Sliding window approach: O(n)
def average_for_subarrays3(array, k):
    _sum, window_start = 0.0, 0
    for window_end in range(len(array)):
        _sum += array[window_end]

        if window_end >= k - 1:
            yield _sum / k
            _sum -= array[window_start]
            window_start += 1


assert list(average_for_subarrays3(array, k)) == [2.2, 2.8, 2.4, 3.6, 2.8]
