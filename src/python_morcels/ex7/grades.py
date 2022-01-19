# way1:
import decimal
import math
import statistics

GRADES = {
    6: 'D',
    7: 'C',
    8: 'B',
    9: 'A',
    10: 'A'
}


def percent_to_grade1(percent: float):
    return GRADES.get(percent // 10, 'F')


# bonus 1, way1
GRADES = [
    (97, 'A+'),
    (93, 'A'),
    (90, 'A-'),
    (87, 'B+'),
    (83, 'B'),
    (80, 'B-'),
    (77, 'C+'),
    (73, 'C'),
    (70, 'C-'),
    (67, 'D+'),
    (63, 'D'),
    (60, 'D-'),
]


def percent_to_grade2(percent, *, suffix=False):
    for min_percent, letter in GRADES:
        if min_percent <= percent:
            return letter if suffix else letter.rstrip('-+')
    return 'F'


# bonus 2 way1
GRADES = [
    (97, 'A+'),
    (93, 'A'),
    (90, 'A-'),
    (87, 'B+'),
    (83, 'B'),
    (80, 'B-'),
    (77, 'C+'),
    (73, 'C'),
    (70, 'C-'),
    (67, 'D+'),
    (63, 'D'),
    (60, 'D-'),
]


def percent_to_grade3(percent, *, suffix=False, round=False):
    if round:
        # using decimal quantize
        percent = decimal.Decimal(percent).quantize(0, decimal.ROUND_HALF_UP)
    for min_percent, letter in GRADES:
        if min_percent <= percent:
            return letter if suffix else letter.rstrip('-+')
    return 'F'


# bonus 2 way2
GRADES = [
    (97, 'A+'),
    (93, 'A'),
    (90, 'A-'),
    (87, 'B+'),
    (83, 'B'),
    (80, 'B-'),
    (77, 'C+'),
    (73, 'C'),
    (70, 'C-'),
    (67, 'D+'),
    (63, 'D'),
    (60, 'D-'),
]


def percent_to_grade4(percent, *, suffix=False, round=False):
    if round and percent % 1 < .5:
        percent = math.floor(percent)
    elif round and percent % 1 >= .5:
        percent = math.ceil(percent)

    for min_percent, letter in GRADES:
        if min_percent <= percent:
            return letter if suffix else letter.rstrip('-+')
    return 'F'


print("Hello")
print(5.4 % 1)


# print(percent_to_grade(96.5, suffix=True, round=True))


# bonus 3 way1
def calculate_gpa1(grades):
    tbl = {
        "A+": 4.33, "A": 4.00, "A-": 3.67,
        "B+": 3.33, "B": 3.00, "B-": 2.67,
        "C+": 2.33, "C": 2.00, "C-": 1.67,
        "D+": 1.33, "D": 1.00, "D-": 0.67,
        "F": 0.00
    }

    return statistics.mean([tbl[grade] for grade in grades])


print(calculate_gpa1(['D+', 'C', 'A-', 'B']))
print(calculate_gpa1(['B+', 'A', 'C+', 'F']))

# bonus 3 way2
GPAS = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0,
}

SIGNS = {
    '-': -0.33,
    '+': +0.33,
}


def calculate_gpa2(grades):
    points = sum(GPAS[g[0]] for g in grades)
    points += sum(SIGNS.get(g[-1], 0) for g in grades)
    return points / len(grades)


# bonus 3 way 3
GPAS = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0,
}

ADJUSTMENT = {
    '-': -0.33,
    ' ': +0.00,
    '+': +0.33,
}


def calculate_gpa(grades):
    grades_with_signs = (
        grade.ljust(2)
        for grade in grades
    )
    points = sum(
        GPAS[letter] + ADJUSTMENT[sign]
        for letter, sign in grades_with_signs
    )
    return points / len(grades)
