import math


def make_squares(array):
    left, right = 0, len(array) - 1
    res = []

    while left < right:
        left_key = array[left] * array[left]
        right_key = array[right] * array[right]

        if left_key > right_key:
            res.append(left_key)
            left += 1
        elif right_key > left_key:
            res.append(right_key)
            right -= 1
        elif right_key == left_key:
            res.append(left_key)
            res.append(right_key)
            right -= 1
            left += 1

    res.append(array[left] * array[left])
    return list(reversed(res))


print(make_squares([-2, -1, 0, 2, 3]))  # Output: [0, 1, 4, 4, 9]
print(make_squares([-3, -1, 0, 1, 2]))  # Output: [0 1 1 4 9]

# print(remove_duplicates([2, 2, 2, 11]))  # 2
