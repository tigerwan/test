def f():
    return 3


def test_function_pass():
    assert f() == 3

def test_function_failure():
    assert f() == 4

