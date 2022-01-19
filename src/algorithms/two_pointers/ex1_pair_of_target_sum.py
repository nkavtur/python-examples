def pair_with_target_sum(array, s):
    start, end = 0, len(array) - 1
    while start != end:
        if array[start] + array[end] < s:
            start += 1
        elif array[start] + array[end] > s:
            end -= 1
        else:
            return (start, end)

    return ()


print(pair_with_target_sum([1, 2, 3, 4, 6], 6))  # Output: [1, 3]
print(pair_with_target_sum([2, 5, 9, 11], 11))  # Output: [0, 2]
