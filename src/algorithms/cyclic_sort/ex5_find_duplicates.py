def find_duplicates(array):
    duplicates = []
    i = 0
    while i < len(array):
        j = array[i] - 1
        if array[j] != array[i]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            duplicates.append(array[i])

    return duplicates


# Output: [4, 5]
print(find_duplicates([3, 4, 4, 5, 5]))

# Output: [3, 5]
print(find_duplicates([5, 4, 7, 2, 3, 5, 3]))
