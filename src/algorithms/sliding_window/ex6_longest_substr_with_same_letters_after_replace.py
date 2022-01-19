from collections import defaultdict


def length_of_longest_substring1(string, k):
    window_start = 0
    seen = defaultdict(int)
    longest = 0
    attemts = k
    key = None

    for window_end in range(len(string)):
        if not key:
            key = string[window_end]

        if key != string[window_end]:
            attemts -= 1

        seen[string[window_end]] += 1
        # print(seen)

        if attemts != -1:
            longest = max(longest, window_end - window_start + 1)

        if attemts == -1:
            while len(seen) >= k + 1:
                # print('shrinking..', seen, len(seen), k + 1, attemts)
                val = seen[string[window_start]]
                if val == 1:
                    del seen[string[window_start]]
                else:
                    seen[string[window_start]] -= 1

                window_start += 1

            attemts = k
            key = string[window_start]

    return longest


# print(length_of_longest_substring1("aabccbb", 2))
# print(length_of_longest_substring1("abbcb", 1))
# print(length_of_longest_substring1("abccde", 1))


def length_of_longest_substring2(string, k):
    window_start = 0
    seen = defaultdict(int)
    longest = 0
    max_repeated_letter = 0

    for window_end in range(len(string)):
        seen[string[window_end]] += 1

        if seen[string[window_end]] > max_repeated_letter:
            max_repeated_letter = seen[string[window_end]]

        if window_end - window_start + 1 - max_repeated_letter > k:
            val = seen[window_start]
            if val == 1:
                del seen[window_start]
            else:
                seen[window_start] -= 1

            window_start += 1

        longest = max(longest, window_end - window_start + 1)

    return longest


print(length_of_longest_substring2("aabccbb", 2))
print(length_of_longest_substring1("abbcb", 1))
print(length_of_longest_substring1("abccde", 1))
