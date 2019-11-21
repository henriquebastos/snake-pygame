from snake.point import Point
from snake.snake import Snake, Directions


def test_snake():
    s = Snake(Point())
    assert s.head == (0, 0)
    assert list(s.tail) == [(1, 0), (2, 0)]
    assert list(s) == [(0, 0), (1, 0), (2, 0)]

def test_slither():
    s = Snake(Point(1, 0))
    assert list(s) == [(1, 0), (2, 0), (3, 0)]
    s.slither()
    assert list(s) == [(0, 0), (1, 0), (2, 0)]

def test_turn():
    s = Snake(Point(0, 0), direction=Directions.LEFT)

    assert s.direction == Directions.LEFT
    s.turn(Directions.RIGHT)
    assert s.direction == Directions.RIGHT
    s.turn(Directions.UP)
    assert s.direction == Directions.UP
    s.turn(Directions.DOWN)
    assert s.direction == Directions.DOWN

def test_eat():
    s = Snake(Point(1, 0))
    assert list(s) == [(1, 0), (2, 0), (3, 0)]
    s.eat()
    assert list(s) == [(1, 0), (2, 0), (3, 0), (0, 0)]
    s.slither()
    assert list(s) == [(0, 0), (1, 0), (2, 0), (3, 0)]
