def binary_search(array, key):
    asc = array[0] < array[1]

    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == key:
            return mid

        if array[mid] > key and asc:
            high = mid - 1
        elif array[mid] > key and not asc:
            low = mid + 1
        elif array[mid] < key and asc:
            low = mid
        elif array[mid] < key and not asc:
            high = mid

    return -1


print(binary_search([4, 6, 10, 11], key=10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], key=5))
print(binary_search([10, 6, 4], key=10))
print(binary_search([10, 6, 4], key=4))
