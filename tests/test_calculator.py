import pytest
from app.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(3, 2) == 5

def test_subtract():
    assert calc.subtract(5, 2) == 3

def test_multiply():
    assert calc.multiply(4, 3) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_factorial():
    assert calc.factorial(5) == 120

def test_power():
    assert calc.power(2, 3) == 8
