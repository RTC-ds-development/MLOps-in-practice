from basic_operations import add_two_integers, multiply_two_floats


def test_add_two_integers():
    assert 4 == add_two_integers(1, 3)


def test_multiply_two_floats():
    assert 1.0 == multiply_two_floats(2.0, 0.5)
