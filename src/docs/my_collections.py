from collections import deque

import itertools
import sys
from math import pi

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# List operations

# fruits[len(fruits):] = ['apple']
fruits.append('apple')
print(fruits)

# fruits[len(fruits):] = ['pineapple', 'pear']
fruits.extend(['pineapple', 'pear'])
print(fruits)

fruits.insert(1, 'watter mellon')
print(fruits)

fruits.remove('banana')
print(fruits)

deleted = fruits.pop(1)
print(deleted, fruits, sep=', ')

deleted = fruits.pop()
print(deleted, fruits, sep=', ')

fruits.sort(key=lambda x: x[1])
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.copy())

fruits.clear()
print(fruits)

# List can act as a stack simply
stack = [3, 1, 2]

stack.append(5)
print(stack)

stack.pop()
print(stack)

# Queue operations

queue = deque([3, 1, 2])

queue.append(10)
print(queue)

queue.popleft()
print(queue)

# List comprehensions

squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

# squares = list(map(lambda x: x ** 2, range(10)))
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

l = [(x, y) for x in [1, 2, 3] for y in (3, 1, 4) if x != y]
print("l eq to ", l)

piList = [str(round(pi, i)) for i in range(1, 10)]
print(piList)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)

transposed = list(zip(*matrix))
print(transposed)

# Del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

mylist = [[1, 2, 3], [4, 5, 6]]
print('zip', *zip(*mylist))

# Sequence Types https://docs.python.org/3/library/stdtypes.html#typesseq
# A sequence is an iterable that you can index starting from 0 until 1 less than the length of the sequence.
# Strings, tuples, and lists are all examples of sequences.
# Sets, dictionaries, files, generators, and lots of other iterables are not sequences.

# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing
empty = ()
print(empty)

single = '1',
print(single)

multiple = 1, '2', 'abc'
print(multiple)

x, y, z = multiple
print(x, y, z)

multiple = ((1, 2, 3, (4, 5)), ['a', 'b', 'c'])
print(multiple)

# set
letters = {'a', 'b', 'c', 'a'}
print(letters)

print('a' in letters)

a = set('abracadabra')
b = set('alacazam')

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# * and ** unpacking examples
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits[1:], fruits[0])
uppercase_fruits = [f.upper() for f in fruits]
print({*fruits, *uppercase_fruits})
print(set().union(fruits, uppercase_fruits))

date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
all_info = {**date_info, **track_info}
print(all_info)

event_info = {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'}
new_info = {**event_info, 'day': "14"}
print(new_info)

a = 123
map = {'a': 1, 'b': 2, 'c': 3}

sequence = [1, 2, 2, 1]

print('all and any:')
print(all(n == m for n, m in zip(sequence, reversed(sequence))))
print(not any(n != m for n, m in zip(sequence, reversed(sequence))))

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print('tel: ')
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

# Keys can be any immutable object - string, number, tuple of strings or numbers or other tuples.
# dict from sequence of tuples
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# dict from **kwargs
dict(sape=4139, guido=4127, jack=4098)

# dict comprehension
map = {x: x ** 2 for x in (2, 4, 6)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print((1, 2, 3, 4) < (1, 2, 4))

numbers = []

# Instead of doing this (it may fail if numbers None)
if len(numbers) == 0:
    print("The numbers list is empty")

# Many of us do this!!!!
if not numbers:
    print("The numbers list is empty")

# iterators

print('size: ')
lots_of_forth = itertools.repeat(4, 1_000_000)
print(sys.getsizeof(lots_of_forth))

lots_of_forth = [4] * 1_000_000
print(sys.getsizeof(lots_of_forth))

for c in itertools.count():  # infinite loop
    if c == 1_000_000:
        print(c)
        break

# file objects are also implemented as iterators
print(next(open('classes.py')))


# implementing custom iterator
class Count:
    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


for c in Count():  # infinite loop
    if c == 1_000_000:
        print(c)
        break

c = Count()
print(next(c))
print(next(c))
print(next(c))

# generators - easy way to create generator
favorite_numbers = [6, 57, 4, 7, 68, 95]


def squares(iterable):
    for num in favorite_numbers:
        yield num ** 2


squares = squares(favorite_numbers)
print(next(squares))
print(next(squares))

squares = (n ** 2 for n in favorite_numbers)
print(next(squares))
print(next(squares))


def gimme4_later_please():
    print("Let me go get that number for you.")
    yield 4


get_four = gimme4_later_please()
print(type(get_four))  # it's generator. yield turns function into generator. It's really magic!!!

print(next(get_four))


# If you find you need an iterator class, try to write a generator function instead

# Note that our Point class here creates an iterable when called (not an iterator), because __next__ is not implemented.
# That means our __iter__ method must return an iterator.
# The easiest way to create an iterator is by making a generator function, so that’s just what we did.
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __iter__(self):
        yield self.x
        yield self.y


# Remember - every iterator is an iterable!!!!!!!! it's super important!!!
# iterators' iterator is itself
a = [1, 2, 3]
iterator1 = iter(a)
iterator2 = iter(iterator1)
assert iterator1 is iterator2

first = next(iterator1)
remaining = [item for item in iterator1]

squares = (n ** 2 for n in range(10))

# islice returns iterator, so we lazy-evaluate our items
for i in itertools.islice(squares, 3):
    print(i)

p = Point(1, 2)
x, y = p
print(x, y)
print(list(p))

# Most of Python’s immutable built-in objects are hashable;
# mutable containers (such as lists or dictionaries) are not;
# immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable.
# Objects which are instances of user-defined classes are hashable by default.
# They all compare unequal (except with themselves), and their hash value is derived from their id().

from collections.abc import Hashable, Sequence, MutableSequence

print(isinstance({}, Hashable))
print(isinstance(0, Hashable))
print(isinstance([], Sequence))
print(issubclass(list, Sequence))
print(issubclass(list, MutableSequence))
print(isinstance((), Sequence))
print(not issubclass(tuple, MutableSequence))
print(isinstance("", Sequence))
print(issubclass(bytearray, MutableSequence))
