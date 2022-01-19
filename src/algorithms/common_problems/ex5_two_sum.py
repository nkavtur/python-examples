from collections import defaultdict


def two_sum(array, s):
    dict = {}
    res = []

    for i, n in enumerate(array):
        diff = s - n
        if diff in dict:
            return dict[diff], i

        dict[n] = i

    return res


print(two_sum([2, 7, 11, 15], 9))
# Output: [0,1]

print(two_sum([3, 2, 4], 6))
# Output: [1,2]

print(two_sum([3, 3], 6))
# Output: [0,1]
