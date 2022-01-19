import math


def remove_duplicates(array):
    next_non_duplicate = 1

    for i in range(1, len(array)):
        if array[i] != array[next_non_duplicate - 1]:
            array[next_non_duplicate] = array[i]
            next_non_duplicate += 1

    return next_non_duplicate

print(remove_duplicates([1, 2, 3, 3, 3, 6, 9, 9, 9]))  # Output: 4
print(remove_duplicates([2, 2, 2, 11]))  # 2


def remove_element(array, key):
    pass


print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))  # Output: 4
print(remove_element([2, 11, 2, 2, 1], 2))  # Output: 2
