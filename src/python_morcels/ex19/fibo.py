def fibonacci(n):
    prev, next = 0, 1
    for i in range(n):
        prev, next = next, prev + next

    return prev


def fibonacci_recursive(n):
    if n in (0, 1):
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci_recursive(7))
