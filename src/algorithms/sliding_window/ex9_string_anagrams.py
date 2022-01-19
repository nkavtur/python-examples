from collections import Counter, defaultdict


def find_string_anagrams(string, pattern):
    window_start, matched, res = 0, 0, []
    char_frequency = defaultdict(int)
    for p in pattern:
        char_frequency[p] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if len(char_frequency) == matched:
            res.append(window_start)

        if window_end - window_start + 1 >= len(pattern):
            left_char = string[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return res


print(find_string_anagrams('ppqp', 'pq'))
print(find_string_anagrams('abbcabc', 'abc'))
