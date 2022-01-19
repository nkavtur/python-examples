def triplet_with_smaller_sum(array, target):
    array.sort()
    count = 0

    for i in range(len(array)):
        count = search_pair(array, count, i + 1, target - array[i])

    return count


def search_pair(array, count, start_index, target):
    left, right = start_index, len(array) - 1
    while left < right:
        if array[left] + array[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
print(triplet_with_smaller_sum([-1, 0, 2, 3], target=3))

# Output: 4
# Explanation: There are four triplets whose sum is less than the target:
# [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], target=5))
