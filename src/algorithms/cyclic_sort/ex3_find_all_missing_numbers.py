def find_all_missing_numbers(array):
    missing_numbers = []
    i = 0
    while i < len(array):
        j = array[i] - 1
        if array[i] != i + 1 and array[i] != array[array[i] - 1]:
            pos1, pos2 = array[i] - 1, i
            array[pos1], array[pos2] = array[pos2], array[pos1]
        else:
            i += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers


# Output: 4, 6, 7
print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))

# Output: 3
print(find_all_missing_numbers([2, 4, 1, 2]))

# Output: 4
print(find_all_missing_numbers([2, 3, 2, 1]))
