class Directions:
    UP = (0, -1)
    DOWN = (0, 1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)


class Snake:
    def __init__(self, head, direction=Directions.LEFT,
                 length=3):
        x, y = head
        self.body = [(x + n, y) for n in range(length)]
        self.direction = direction

    def __getitem__(self, item):
        return self.body[item]

    def __setitem__(self, key, value):
        self.body[key] = value

    def slither(self):
        for i in range(len(self.body) - 1, 0, -1):
            self[i] = (self[i - 1][0], self[i - 1][1])

        self[0] = (self[0][0] + self.direction[0],
                   self[0][1] + self.direction[1])

    def turn(self, direction):
        self.direction = direction

    def eat(self):
        self.body.append((0, 0))
