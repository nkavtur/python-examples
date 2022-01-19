def is_happy_number(num):
    fast = find_square(find_square(num))
    slow = find_square(num)

    while fast != slow:
        fast = find_square(find_square(fast))
        slow = find_square(slow)

        if fast == 1 or slow == 1:
            return True

    return False

def find_square(num):
    res = 0
    for d in to_digits(num):
        res += d * d
    return res


def to_digits(num):
    res = []
    while num // 10 > 0:
        res.append(num % 10)
        num = num // 10

    res.append(num % 10)
    return list(reversed(res))


print('LinkedList cycle start: ', is_happy_number(23))
print('LinkedList cycle start: ', is_happy_number(12))
