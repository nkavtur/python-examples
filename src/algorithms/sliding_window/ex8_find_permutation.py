from collections import defaultdict


def find_permutation1(string, pattern):
    window_start, matched = 0, 0

    pattern_dict = defaultdict(int)
    for p in pattern:
        pattern_dict[p] += 1

    for window_end in range(len(string)):
        if string[window_end] not in pattern_dict:
            while window_start != window_end:
                matched -= 1
                pattern_dict[string[window_start]] += 1
                window_start += 1
            window_start += 1
            continue

        pattern_dict[string[window_end]] -= 1
        if pattern_dict[string[window_end]] >= 0:
            matched += 1
        elif pattern_dict[string[window_end]] < 0:
            window_start += 1
            pattern_dict[string[window_end]] += 1

        if len(pattern) == matched:
            return True

    return False


print(find_permutation1('oidacaf', 'acc'))
print(find_permutation1('oidabcf', 'abc'))
print(find_permutation1('odicf', 'dc'))
print(find_permutation1('bcdxabcdy', 'bcdyabcdx'))
print(find_permutation1('aaacb', 'abc'))
print(find_permutation1('abiaacb', 'abc'))


def find_permutation2(string, pattern):
    window_start, matched = 0, 0
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
            return True

        if window_end - window_start + 1 >= len(pattern):
            left_char = string[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


print()
print(find_permutation2('oidacaf', 'acc'))
print(find_permutation2('oidabcf', 'abc'))
print(find_permutation2('odicf', 'dc'))
print(find_permutation2('bcdxabcdy', 'bcdyabcdx'))
print(find_permutation2('aaacb', 'abc'))
print(find_permutation2('abiaacb', 'abc'))
