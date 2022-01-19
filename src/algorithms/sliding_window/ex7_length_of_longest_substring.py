from collections import defaultdict


def length_of_longest_substring(array, k):
    window_start = 0
    frequency = defaultdict(int)
    max_length = 0

    for window_end in range(len(array)):
        frequency[array[window_end]] += 1

        while frequency[0] > k:
            val = frequency[array[window_start]]
            if val == 1:
                del frequency[array[window_start]]
            else:
                frequency[array[window_start]] -= 1

            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


