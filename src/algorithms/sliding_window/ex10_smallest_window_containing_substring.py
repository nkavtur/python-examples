import math
from collections import defaultdict


def find_substring(string, pattern):
    window_start, matched, start = 0, 0, 0
    min_length = math.inf

    char_frequency = defaultdict(int)
    for p in pattern:
        char_frequency[p] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

            if matched == len(char_frequency):
                if window_end - window_start + 1 < min_length:
                    min_length = window_end - window_start + 1
                    start = window_start

            if char_frequency[right_char] < 0:
                while window_start != window_end:
                    left_char = string[window_start]
                    window_start += 1
                    if left_char in char_frequency:
                        if char_frequency[left_char] == 0:
                            matched -= 1
                        char_frequency[left_char] += 1

    if min_length == math.inf:
        return ""
    return string[start:start + min_length]


print(find_substring("aabdecabc", "abc"))  # "abdec"
print(find_substring("aabdec", "abc"))  # "abdec"
print(find_substring("abdabca", "abc"))  # "abc"
print(find_substring("adcad", "abc"))  # ""
