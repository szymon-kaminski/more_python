from divide_integers import divide


def test_case1():
    assert divide(10 / 5) == 2


def test_case2():
    assert divide(10 / 0) == "Not defined"


def test_case3():
    assert divide(10 / 3) == 3


def test_case4():
    assert divide(None, 3) == 'Numerator/denominator value is None'