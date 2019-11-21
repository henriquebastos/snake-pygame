from collections import namedtuple
from random import randrange

from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT

from snake.settings import WIDTH, HEIGHT


class Point(namedtuple('Point', ['x', 'y'], defaults=[0, 0])):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    @classmethod
    def random(cls):
        return Point(randrange(WIDTH-1), randrange(HEIGHT-1))


class Directions:
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    RIGHT = Point(1, 0)
    LEFT = Point(-1, 0)

    direction_for_key = {
        K_UP: UP,
        K_DOWN: DOWN,
        K_RIGHT: RIGHT,
        K_LEFT: LEFT,
    }

    @classmethod
    def by(cls, key_event):
        return cls.direction_for_key[key_event]
