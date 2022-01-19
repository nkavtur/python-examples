def find_first_missing_positive(array):
    i = 0
    while i < len(array):
        if array[i] < 0:
            i += 1
            continue

        j = array[i] - 1
        if j < len(array) and array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            return i + 1


# Output: 3
print(find_first_missing_positive([-3, 1, 5, 4, 2]))

# Output: 4
print(find_first_missing_positive([3, -2, 0, 1, 2]))

# Output: 4
print(find_first_missing_positive([3, 2, 5, 1]))
