from collections import deque, namedtuple

from snake.geometry import Point, Directions


class Apple(Point):
    pass


class Snake:
    def __init__(self, head, direction=Directions.LEFT,
                 length=3):
        self.head = head
        self.tail = deque(head + Point(n, 0) for n in range(1, length))
        self.direction = direction

    def __getitem__(self, item):
        return self.tail[item-1] if item else self.head

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
