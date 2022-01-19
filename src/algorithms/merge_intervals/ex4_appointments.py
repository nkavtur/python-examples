def can_attend_all_appointments(appointments):
    start, end = 0, 1
    appointments.sort(key=lambda a: a[start])
    print(appointments)

    prev = appointments[0]
    for i in range(1, len(appointments)):
        current = appointments[i]
        if prev[end] > current[start]:
            return False
        prev = current

    return True


# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
print(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))

# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.
print(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))

# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
print(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
