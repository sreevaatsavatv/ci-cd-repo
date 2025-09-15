import pytest
from app.calculator import Calculator
from app.textprocessor import TextProcessor

calc = Calculator()
tp = TextProcessor()

def test_combined_usage():
    # Calculator
    assert calc.add(2, 3) == 5
    assert calc.power(2, 4) == 16

    # TextProcessor
    text = "level"
    assert tp.is_palindrome(text) is True
    assert tp.reverse_text("abc") == "cba"
