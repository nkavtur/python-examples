from collections import defaultdict, deque


def non_repeat_substring1(string):
    window_start = 0
    seen = defaultdict(int)
    max_substr = deque()
    current_substr = deque()

    for window_end in range(len(string)):
        current_substr.append(string[window_end])
        seen[string[window_end]] += 1

        if len(max_substr) < len(current_substr) and seen[string[window_end]] <= 1:
            max_substr.clear()
            max_substr += current_substr

        while seen[string[window_end]] > 1:
            val = seen[string[window_start]]
            if val == 1:
                seen.pop(string[window_start])
            else:
                seen[string[window_start]] -= 1

            current_substr.popleft()
            window_start += 1

    return max_substr


print(non_repeat_substring1("caabccbb"))
print(non_repeat_substring1("abbbb"))
print(non_repeat_substring1("abccde"))

