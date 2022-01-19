import sys

print(sys.argv)

str = 'Hello World'
print(str[:])

array = [1, 2, 3, 4, 5, 6]
array[1:3] = [9, 8]
print(array)


def f(n):
    if n in (1, 0):
        return n
    return n * f(n - 1)


print(f(5))

users = {'john': 'active', 'bryan': 'inactive'}
print(users.copy().items())

for name, status in users.copy().items():
    if status == 'inactive':
        del users[name]

print(users)


def ask_ok(promt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(promt)
        if ok in ('y', 'yes', 'ye'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


retries = 5

print(ask_ok('enter y/no', retries), retries)


# example of using namespace with scope
def f(a, l=[]):
    l.append(a)
    return l


print(f(1))
print(f(2))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(state='Hello', voltage=10)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def standard_arg(arg):
    print(arg)


def pos_arg(arg, /):
    print(arg)


def kw_arg(*, arg):
    print(arg)


def combination_args(arg1, /, arg2, *, arg3):
    print(arg1, arg2, arg3)


standard_arg(1)
standard_arg(arg=1)

pos_arg(1)
# pos_arg(arg=1)

kw_arg(arg=1)

combination_args(1, arg2=2, arg3=3)


def f(name, /, **kwargs):
    print('name' in kwargs)


f(1, name='hello', surname='hi')


def concat(*args, sep="/"):
    return sep.join(args)


print(concat('hello', 'hi', 'greetings', sep='.'))
print(*range(3, 6))

print(*[9, 7, 8], sep=' / ')

print(*zip(*[[1, 2], [3, 4], [5, 6]]))

print()

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
first, second, *remaining = fruits
print(remaining)

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
((first_letter, *remaining), *other_fruits) = fruits
print(remaining)

# By default, Python’s == operator delegates to is.
# Meaning unless two variables point to the exact some object in memory, == will return False:
x = None
print(x is None)
print(x == None)  # wrong because None is singleton like True/False, object()


# Each object can customize the behavior of == to answer whatever question they’d like.
# For that we need to overload __eq__
class AlwaysEqual:
    def __eq__(self, other):
        return True
