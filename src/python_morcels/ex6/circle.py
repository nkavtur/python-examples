from math import pi


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value: int):
        self.radius = value / 2

    @property
    def area(self):
        return pi * (self.radius ** 2)

    def __repr__(self) -> str:
        return f"Circle({self.radius})"


c = Circle(5)
print(c.diameter)
print(c.area)
print(c)

c = Circle()
print(c.radius)
print(c.diameter)

c.radius = 10
print(c.diameter)
print(c.area)

c.diameter = 5
print(c.radius)
print(c.area)
