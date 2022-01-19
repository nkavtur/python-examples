from typing import List


# array = [1, 9, 0, 4, 3, 5]
def insertion_sort(array: List) -> List:
    for i in range(1, len(array)):
        key, j = array[i], i
        while (j := j - 1) >= 0 and key < array[j]:
            array[j + 1] = array[j]
        array[j + 1] = key

    return array


def selection_sort(array: List) -> List:
    for i in range(0, len(array)):

        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


def merge_sort(array: List) -> List:
    if len(array) == 1:
        return array

    if len(array) == 2 and array[0] > array[1]:
        array[0], array[1] = array[1], array[0]

    left_size = len(array) // 2 + len(array) % 2
    right_size = len(array) // 2

    left = merge_sort(array[:left_size])
    right = merge_sort(array[len(array) - right_size:])

    return merge(left, right)


def merge(left, right):
    merged = [] # 1
    k, i, j = 0, 0, 0 # 2
    while k < len(left) + len(right): # 3

        if i >= len(left):
            right_tail = right[j:]
            merged += right_tail
            k += len(right_tail)
            continue

        if j >= len(right):
            left_tail = left[i:]
            merged += left_tail
            k += len(left_tail)
            continue

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

        k += 1

    return merged


def bubble_sort(array: List) -> List:
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array


array = [9, 1, 0, 4, 3, 5, 0, 0]

assert sorted(array) == insertion_sort(array)
assert sorted(array) == selection_sort(array)
assert sorted(array) == merge_sort(array)
assert sorted(array) == bubble_sort(array)
