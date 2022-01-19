def sort_and_count_inversions(array):
    if len(array) == 1:
        return array, 0

    left, left_inversions = sort_and_count_inversions(array[:len(array) // 2])
    right, right_inversions = sort_and_count_inversions(array[len(array) // 2:])

    merged, split_inversions = merge_and_count_inversions(left, right)
    return merged, split_inversions + left_inversions + right_inversions


def merge_and_count_inversions(left, right):
    i, j, k = 0, 0, 0
    res = []
    inversions = 0

    while k < len(left) + len(right):

        if i == len(left):
            res += right[j:]
            break

        if j == len(right):
            res += left[i:]
            break

        if left[i] < right[j]:
            res.append(left[i])
            i += 1
            continue

        if right[j] < left[i]:
            res.append(right[j])
            j += 1
            inversions += len(left) - i
            continue

        k += 1

    return res, inversions


_, inversions = sort_and_count_inversions([8, 4, 2, 1])
assert inversions == 6

_, inversions = sort_and_count_inversions([3, 1, 2])
assert inversions == 2
