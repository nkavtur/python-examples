from collections import defaultdict


def find_first_unique_character(text):
    frequency = defaultdict(int)

    for c in text:
        frequency[c] += 1

    for c in text:
        if frequency[c] == 1:
            return c

    return -1



# Output: l
print(find_first_unique_character("leetcode"))

# Output: v
print(find_first_unique_character("loveleetcode"))

# Output: -1
print(find_first_unique_character("aabb"))
