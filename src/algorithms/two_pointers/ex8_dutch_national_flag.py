def dutch_flag_sort(array):
    start, end = 0, len(array) - 1

    i = 0
    while i <= end:
        # print(array, i, (start, end))

        if array[i] == 0:
            array[start], array[i] = array[i], array[start]
            start += 1
            i += 1
            continue

        if array[i] == 2:
            array[end], array[i] = array[i], array[end]
            end -= 1
            # i += 1
            continue

        i += 1

    return array


# Output: [0 0 1 1 2]
print(dutch_flag_sort([1, 0, 2, 1, 0]))

# Output: [0 0 1 2 2 2 ]
print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
