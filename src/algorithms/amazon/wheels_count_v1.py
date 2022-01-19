def fleet_count(wheels):
    if wheels == 2:
        return 1

    if wheels == 4:
        return 2

    count = [0]
    seen = set()
    current_path = []
    fleet_count_recursively(wheels, count, current_path, seen)
    print(seen)
    return len(seen)


def fleet_count_recursively(wheels, count, current_path, seen):
    if wheels <= 0:
        seen.add(tuple(sorted(current_path)))
        return

    if wheels == 2:
        current_path.append(2)
        wheels -= 2
        seen.add(tuple(sorted(current_path)))
        wheels += current_path.pop()
        return

    current_path.append(2)
    wheels -= 2
    fleet_count_recursively(wheels, count, current_path, seen)
    wheels += current_path.pop()

    if wheels >= 4:
        current_path.append(4)
        wheels -= 4
        fleet_count_recursively(wheels, count, current_path, seen)
        wheels += current_path.pop()


print(fleet_count(14))
