import pytest
from fonction import add, divide, multiply

def test_add():
    assert add(3,4) == 7
    assert add("a","b") == "ab"
    assert add(3.2,5.3) == 8.5

def test_multiply():
    assert multiply(20,0) == 0
    assert multiply(2,6) == 12

def test_divide():
    assert divide(20,4) == 5
    with pytest.raises(ZeroDivisionError): divide(0,0)

@pytest.mark.parametrize("numerator, denominator, result", [(2, 2, 4), ("a", "b", "ab"), (3.2, 5.3, 8.5)])
def test_should_return_square(numerator, denominator, result):
    assert add(numerator,denominator) == result