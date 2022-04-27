# way 1 + bonus 1
def multimax(iterable):
    max_item = max(iterable, default=None)
    return [
        item
        for item in iterable
        if item == max_item
    ]


assert multimax([2, -10, 3, 1, 3]) == [3, 3]
assert multimax([]) == []


# way 1 bonus1 + bonus2
def multimax(iterable, key=lambda x: x):
    max_score = None
    maximums = []

    for item in iterable:
        score = key(item)
        if not maximums or score > max_score:
            maximums = [item]
            max_score = score
        elif score == max_score:
            maximums.append(item)
    return maximums


assert multimax([2, -10, 3, 1, 3]) == [3, 3]
assert multimax([]) == []

# inputs = [[0], [1], [], [0, 1], [1]]
# expected = [[1], [1]]
# assert multimax(inputs, key=len) == expected


numbers = [1, 3, 8, 5, 4, 10, 6]
odds = (n for n in numbers if n % 2 == 1)
assert multimax(odds) == [5]

words = ["ministry", "of", "silly", "walks", "argument", "clinic"]
assert multimax(words, key=len) == ['ministry', 'argument']
