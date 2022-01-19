import math
from collections import defaultdict


def longest_substring_with_k_distinct(string, k):
    window_start, window_end = 0, 0
    res = string

    letters_seen, number_of_letters = defaultdict(int), math.inf

    for window_end in range(len(string)):
        letters_seen[string[window_end]] += 1
        number_of_letters += 1

        if len(letters_seen) == k:
            res = res if number_of_letters < window_end + 1 - window_start else string[window_start:window_end + 1]

        while len(letters_seen) > k:
            val = letters_seen[string[window_start]]
            if val == 1:
                letters_seen.pop(string[window_start])
                number_of_letters -= 1
            else:
                letters_seen[string[window_start]] -= 1

            window_start += 1

    return res


assert longest_substring_with_k_distinct('araaci', 2) == 'araa'
assert longest_substring_with_k_distinct('araaci', 1) == 'aa'
assert longest_substring_with_k_distinct('cbbebi', 3) == 'cbbeb'
