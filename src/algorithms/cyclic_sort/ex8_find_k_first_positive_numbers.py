def find_first_k_missing_positive(array, k):
    res = []
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

    biggest_seen = 0
    for i in range(len(array)):
        biggest_seen = max(biggest_seen, array[i])
        if array[i] != i + 1:
            res.append(i + 1)
        if len(res) == k:
            return res

    for j in range(1, k - len(res) + 1):
        res.append(biggest_seen + j)

    return res


# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
print(find_first_k_missing_positive([3, -1, 4, 5, 5], k=3))

# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.
print(find_first_k_missing_positive([2, 3, 4], k=3))

# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.
print(find_first_k_missing_positive([-2, -3, 4], k=2))
