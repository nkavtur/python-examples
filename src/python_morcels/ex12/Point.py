# way1

class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, scalar):
        return Point(*(scalar * coordinate for coordinate in self))

    __rmul__ = __mul__

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    def __eq__(self, o):
        return tuple(self) == tuple(o)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"


p1 = Point(1, 2, 3)
assert str(p1) == 'Point(x=1, y=2, z=3)'

p2 = Point(1, 2, 3)
assert p1 == p2

p2.x = 4
assert not (p1 == p2)

assert str(p2) == 'Point(x=4, y=2, z=3)'

p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

assert str(p1 + p2) == 'Point(x=5, y=7, z=9)'
assert str(p2 - p1) == 'Point(x=3, y=3, z=3)'

p1 = Point(1, 2, 3)
p2 = p1 * 2
assert str(p2) == 'Point(x=2, y=4, z=6)'

p1 = Point(1, 2, 3)
x, y, z = p1
assert (x, y, z) == (1, 2, 3)

# way2
from dataclasses import dataclass, astuple


@dataclass
class Point:
    x: float
    y: float
    z: float

    def __add__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, scalar):
        return Point(*(scalar * coordinate for coordinate in self))

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)


p1 = Point(1, 2, 3)
assert str(p1) == 'Point(x=1, y=2, z=3)'

p2 = Point(1, 2, 3)
assert p1 == p2

p2.x = 4
assert not (p1 == p2)

assert str(p2) == 'Point(x=4, y=2, z=3)'

p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

assert str(p1 + p2) == 'Point(x=5, y=7, z=9)'
assert str(p2 - p1) == 'Point(x=3, y=3, z=3)'

p1 = Point(1, 2, 3)
p2 = p1 * 2
assert str(p2) == 'Point(x=2, y=4, z=6)'

p1 = Point(1, 2, 3)
x, y, z = p1
assert (x, y, z) == (1, 2, 3)
