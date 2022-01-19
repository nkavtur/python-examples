import math


def triplet_sum_close_to_target(array, target):
    array.sort()
    triplets = []
    for i in range(len(array)):
        search_pair(target - array[i], array[i], i + 1, array, triplets)

    res = sorted(triplets, key=lambda triplet: math.fabs(target - (triplet[0] + triplet[1] + triplet[2])))

    return res[0], sum(res[0])


def search_pair(target, first, start_index, array, triplets):
    left, right = start_index, len(array) - 1
    min_diff = math.inf

    while left < right:
        current_diff = target - array[left] - array[right]

        if current_diff < min_diff:
            min_diff = current_diff
            triplets.append((first, array[left], array[right]))
            left += 1
        elif current_diff > min_diff:
            right -= 1
        elif current_diff == min_diff:
            left += 1
            right -= 1

    return min_diff


# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
print(triplet_sum_close_to_target([-2, 0, 1, 2], target=2))

# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
print(triplet_sum_close_to_target([-3, -1, 1, 2], target=1))

# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.
print(triplet_sum_close_to_target([1, 0, 1, 1], target=100))
