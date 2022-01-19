from enum import Enum, auto, unique, IntEnum, IntFlag, Flag
from collections.abc import Hashable


@unique
class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = auto()
    PURPLE = 4
    # PURPLE_ALIAS = 4


assert Colors(2) == Colors.GREEN
assert Colors(2) == Colors['GREEN']

assert Colors(3) == Colors.BLUE
assert Colors(3) == Colors['BLUE']

assert Colors(4) == Colors.PURPLE
assert Colors(4) == Colors['PURPLE']

color = Colors.GREEN
assert color.name == 'GREEN'
assert color.value == 2

for color in Colors:
    print(color)

assert isinstance(Colors.RED, Hashable)


# it's possible to customize auto:
class NameEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Ordinal(NameEnum):
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    EAST = auto()


assert Ordinal.NORTH.value == 'NORTH'

# enumeration for enums:
assert list(Ordinal) == [Ordinal.NORTH, Ordinal.SOUTH, Ordinal.WEST, Ordinal.EAST]

assert list(Ordinal.__members__.items()) == [('NORTH', Ordinal.NORTH), \
                                             ('SOUTH', Ordinal.SOUTH), \
                                             ('WEST', Ordinal.WEST), \
                                             ('EAST', Ordinal.EAST)]


# enum can have other methods:
class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        # self is the member here
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY


# Pickling:
from pickle import dumps, loads

assert loads(dumps(Colors.RED)) == Colors.RED

# Functional API
Animal = Enum('Animal', 'TIGER LION')
print(Animal.TIGER)


# int enum is a subclass of int:
class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2


assert int(Shape.SQUARE) == 2


# int flag enum is also subclass of int, but bitwise operations can be used here:
class Perm(IntFlag):
    NO = 0
    R = 4
    W = 2
    X = 1
    RWX = 7


assert Perm.X not in Perm.R | Perm.W
assert Perm.R in Perm.R | Perm.W

assert Perm.R + Perm.W + Perm.X == Perm.RWX
assert Perm.R | Perm.W | Perm.X == Perm.RWX

assert not bool(Perm.X & Perm.R)  # results to false because no such flag in enum
assert bool(Perm.X | Perm.R)  # results to true because flag in enum

assert Perm.R & Perm.X == Perm.NO == 0  # because we are using IntFlagEnum the result is int


# flag enum also allow bitwise operations
class Color(Flag):
    BLACK = 0
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    WHITE = RED | BLUE | GREEN


assert not bool(Color.RED & Color.GREEN)  # results to false because no such flag in enum
assert bool(Color.RED | Color.GREEN)  # results to true because flag in enum

assert Color.RED & Color.GREEN == Color.BLACK != 0  # because we are using FlagEnum the result is not int
assert Color.WHITE.value == 7


# using init with enum
class Planet(Enum):

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    EARTH = (123, 456)
    MARS = (124, 457)


assert Planet.EARTH.mass == 123
assert Planet.EARTH.value == (123, 456)
