from snake.snake import Snake, Directions


def test_snake():
    s = Snake((0, 0))
    assert s.body == [(0, 0), (1, 0), (2, 0)]
    assert (s[0], s[1], s[2]) == ((0, 0), (1, 0), (2, 0))
    s[0] = (0, 1)
    assert s[0] == (0, 1)

def test_slither():
    s = Snake((1, 0))
    assert s.body == [(1, 0), (2, 0), (3, 0)]
    s.slither()
    assert s.body == [(0, 0), (1, 0), (2, 0)]

def test_turn():
    s = Snake((0, 0), direction=Directions.LEFT)

    assert s.direction == Directions.LEFT
    s.turn(Directions.RIGHT)
    assert s.direction == Directions.RIGHT
    s.turn(Directions.UP)
    assert s.direction == Directions.UP
    s.turn(Directions.DOWN)
    assert s.direction == Directions.DOWN

def test_eat():
    s = Snake((1, 0))
    assert s.body == [(1, 0), (2, 0), (3, 0)]
    s.eat()
    assert s.body == [(1, 0), (2, 0), (3, 0), (0, 0)]
    s.slither()
    assert s.body == [(0, 0), (1, 0), (2, 0), (3, 0)]
