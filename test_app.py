import time
import pytest
from app import Calculator, TextProcessor

calc = Calculator()
tp = TextProcessor()

# Calculator tests
def test_add():
    time.sleep(2)
    assert calc.add(10, 5) == 15

def test_subtract():
    time.sleep(2)
    assert calc.subtract(10, 5) == 5

def test_multiply():
    time.sleep(2)
    assert calc.multiply(3, 4) == 12

def test_divide():
    time.sleep(2)
    assert calc.divide(10, 2) == 5

def test_factorial():
    time.sleep(2)
    assert calc.factorial(5) == 120

def test_power():
    time.sleep(2)
    assert calc.power(2, 3) == 8


# Text Processor tests
def test_word_count():
    time.sleep(2)
    assert tp.word_count("Hello world") == 2

def test_char_count():
    time.sleep(2)
    assert tp.char_count("Hello") == 5

def test_reverse_text():
    time.sleep(2)
    assert tp.reverse_text("abcd") == "dcba"

def test_palindrome():
    time.sleep(2)
    assert tp.is_palindrome("madam") is True
