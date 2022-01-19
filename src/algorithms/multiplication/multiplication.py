# n = 4
# x = 5678
# y = 1234

# a = 56, b =78
# c = 12, d = 34

# x = 10^(n/2) * a + b
# y = 10^(n/2) * c + d
# x * y = (10^(n/2) * a + b) * (10^(n/2) * c + d) = 10^n * ac + 10^(n/2) * (ad + bc) + bd

# 1: compute ac
# 2: compute bd
# 3: compute (a + b) * (c + d) = ac + ad + bc + bd
# 4: (3) - (2) - (1)

# res = 10^n * ac + 10^(n/2) * (4) + bd

def digits(x):
    n = 0
    while (x := x // 10) > 0:
        n += 1
    return n + 1


def pow(x, n):
    res = x
    for i in range(1, n):
        res *= x
    return res


def кaratsuba_multiply(x, y):
    n = digits(x)

    if n == 1:
        return x * y

    n_2 = n // 2

    a = x // pow(10, n_2)
    b = x % pow(10, n_2)

    c = y // pow(10, n_2)
    d = y % pow(10, n_2)

    ac = кaratsuba_multiply(a, c)
    bd = кaratsuba_multiply(b, d)

    return pow(10, n - (n % 2)) * ac + pow(10, n_2) * (кaratsuba_multiply(a + b, c + d) - ac - bd) + bd


x = 123456
y = 567890
assert кaratsuba_multiply(x, y) == x * y
