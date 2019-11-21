from collections import deque

from snake.point import Point


class Directions:
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    RIGHT = Point(1, 0)
    LEFT = Point(-1, 0)


class Snake:
    def __init__(self, head, direction=Directions.LEFT,
                 length=3):
        self.head = head
        self.tail = deque(head + Point(n, 0) for n in range(1, length))
        self.direction = direction

    def __getitem__(self, item):
        if item == 0:
            return self.head
        else:
            return self.tail[item-1]

    def __len__(self):
        return len(self.tail) + 1

    def slither(self):
        self.tail.appendleft(self.head)
        self.tail.pop()
        self.head += self.direction

    def turn(self, direction):
        if self.direction + direction == Point(0, 0):
            return

        self.direction = direction

    def eat(self):
        self.tail.append(Point(0, 0))
