from snake.characters import Point


def test_point():
    p = Point(0, 0)
    assert p.x == 0
    assert p.y == 0

def test_add():
    assert Point(1, 0) + Point(0, 1) == Point(1, 1)

def test_mul():
    assert Point(1, 1) * 10 == Point(10, 10)
