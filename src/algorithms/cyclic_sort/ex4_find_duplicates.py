def find_duplicates(array):
    i = 0
    guard = 0
    while i < len(array) and guard < 10:
        print(array, i)
        if array[array[i] - 1] != array[i]:
            pos1, pos2 = i, array[i] - 1
            array[pos1], array[pos2] = array[pos2], array[pos1]
        else:
            i += 1

        guard += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            return array[i]


# Output: 4
print(find_duplicates([3, 4, 4, 4, 1]))

# Output: 3
# print(find_duplicates([2, 1, 3, 3, 5, 4]))

# Output: 4
# print(find_duplicates([2, 4, 1, 4, 4]))
