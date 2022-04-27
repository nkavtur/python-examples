ROMAN_TO_ARABIC = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

ARABIC_TO_ROMAN = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

BASE_NUMBERS = list(reversed(sorted(ARABIC_TO_ROMAN.keys())))


def int_to_roman(n):
    res = ''

    for base in BASE_NUMBERS:
        x, n = divmod(n, base)
        res += ARABIC_TO_ROMAN[base] * x

    return res


print(int_to_roman(4) == 'IV')
print(int_to_roman(9) == 'IX')
print(int_to_roman(1999) == 'MCMXCIX')


def roman_to_int(roman_number):
    if not set(roman_number).issubset(ROMAN_TO_ARABIC.keys()):
        raise ValueError("Invalid symbols in Roman numeral")

    result = 0

    i = 0
    for symbol, value in ROMAN_TO_ARABIC.items():
        while roman_number[i:i + len(symbol)] == symbol:
            result += value
            i += len(symbol)

    return result


print(roman_to_int('IV') == 4)
print(roman_to_int('MCMXLVIII') == 1948)
