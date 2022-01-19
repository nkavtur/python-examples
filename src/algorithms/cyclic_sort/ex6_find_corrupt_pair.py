def find_corrupt_pair(array):
    i = 0

    while i < len(array):
        j = array[i] - 1
        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            return array[i], i + 1


# Output: [2, 4]
print(find_corrupt_pair([3, 1, 2, 5, 2]))

# Output: [3, 5]
print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))
