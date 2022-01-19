from collections import deque


def find_subarrays1(array, target):
    window_start, window_end = 0, 0
    current_product = 1
    res = []

    while window_end < len(array):
        current_product *= array[window_end]

        if current_product < target:
            res.append(array[window_start: window_end + 1])

            if window_end == len(array) - 1:
                window_start += 1
                window_end = window_start - 1
                current_product = 1

        else:
            window_start += 1
            window_end = window_start - 1
            current_product = 1

        window_end += 1

    return res


# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# print(find_subarrays1([2, 5, 3, 10], target=30))

# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
# Explanation: There are seven contiguous subarrays whose product is less than the target.
# print(find_subarrays1([8, 2, 6, 5], target=50))


def find_subarrays2(array, target):
    window_start, window_end = 0, 0
    current_product = 1
    res = []

    for window_end in range(len(array)):
        current_product *= array[window_end]

        while current_product >= target and window_start != len(array) - 1:
            current_product /= array[window_start]
            window_start += 1

        temp_res = deque()
        for j in range(window_end, window_start - 1, -1):
            temp_res.appendleft(array[j])
            print(list(temp_res))
            res.append(list(temp_res))

    return res


print()
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# print(find_subarrays2([2, 5, 3, 10], target=30))
find_subarrays2([2, 5, 3, 10], target=30)

# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
# Explanation: There are seven contiguous subarrays whose product is less than the target.
# print(find_subarrays2([8, 2, 6, 5], target=50))
