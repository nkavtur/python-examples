def cyclic_sort(array):
    i = 0
    while i < len(array):
        current = array[i]
        while i + 1 != current:
            array[i], array[current - 1] = array[current - 1], array[i]
            current = array[i]
        i += 1

    return array


print(cyclic_sort([3, 1, 5, 4, 2]))

print(cyclic_sort([2, 6, 4, 3, 1, 5]))

print(cyclic_sort([1, 5, 6, 4, 3, 2]))
