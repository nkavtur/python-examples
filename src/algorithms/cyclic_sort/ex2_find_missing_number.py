def find_missing_number(array):
    i = 0

    while i < len(array):
        if array[i] != i and array[i] < len(array):
            pos1, pos2 = i, array[i]
            array[pos1], array[pos2] = array[pos2], array[pos1]
        else:
            i += 1

    for i in range(0, len(array)):
        if array[i] != i:
            return i

    return len(array)


# Output: 2
print(find_missing_number([4, 0, 3, 1]))

# Output: 7
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
