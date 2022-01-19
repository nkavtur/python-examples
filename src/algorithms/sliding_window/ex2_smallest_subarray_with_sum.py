import math

array = [1, 1, 5, 2, 3, 2]
s = 7


# BruteForce: O(n^2)
def find_min_array1(array, s):
    min_array = None
    for i in range(len(array)):
        _sum = 0

        current_min_array = []
        for j in range(i, len(array)):
            _sum += array[j]
            current_min_array.append(array[j])
            if _sum == s:
                if min_array:
                    if len(min_array) > len(current_min_array):
                        min_array = current_min_array
                else:
                    min_array = current_min_array
                break

    return min_array


assert find_min_array1(array, s) == [5, 2]


# Sliding window time complexity O(n), space complexity - O(1)
def find_min_array2(array, s):
    window_start, window_end, window_sum = 0, 0, 0
    res = array

    for window_end in range(len(array)):
        window_sum += array[window_end]

        while window_sum >= s:
            current = array[window_start:window_end + 1]
            res = res if len(res) < len(current) else current
            window_sum -= array[window_start]
            window_start += 1

    return res


assert find_min_array2([2, 1, 5, 2, 3, 2], 7) == [5, 2]
assert find_min_array2([2, 1, 5, 2, 8], 7) == [8]
assert find_min_array2([3, 4, 1, 1, 6], 8) == [1, 1, 6]
