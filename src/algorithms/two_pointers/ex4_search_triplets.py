def search_triplets(array):
    array.sort()
    triplets = []

    for i in range(len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue
        search_pair(-array[i], i + 1, array, triplets)

    return triplets


def search_pair(s, start_index, array, triplets):
    left, right = start_index, len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == s:
            triplets.append([-s, array[left], array[right]])
            left += 1
            right -= 1
            while left < right and array[left] == array[left - 1]:
                left += 1
            while left < right and array[right] == array[right + 1]:
                right -= 1

        if current_sum < s:
            left += 1
        elif current_sum > s:
            right -= 1


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))  # Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
print(search_triplets([-5, 2, -1, -2, 3]))  # Output: [[-5, 2, 3], [-2, -1, 3]]
