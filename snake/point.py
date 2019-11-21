from collections import  namedtuple


class Point(namedtuple('Point', ['x', 'y'], defaults=[0, 0])):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
