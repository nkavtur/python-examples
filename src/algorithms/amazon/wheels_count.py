from collections import deque


def fleet_count(wheels):
    queue = deque([])
    wheels_copy = wheels
    count = 1
    while wheels_copy > 0:
        wheels_copy -= 2
        queue.append(2)

    count = 1
    while len(queue) >= 2 and queue[-1] != 4:
        last, pre_last = queue.pop(), queue.pop()

        if last != 2 or pre_last != 2:
            break

        queue.appendleft(4)
        count += 1

    return count


def fleet_count1(wheels):
    count = 1
    while wheels > 2:
        if wheels % 2 == 0:
            wheels = wheels - 4
        else:
            wheels -= 2
        count += 1

    return count


wheels = 40
print(fleet_count(wheels))
print(fleet_count1(wheels))
