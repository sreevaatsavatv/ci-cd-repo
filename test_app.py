import time
from app import add, multiply

def test_add():
    time.sleep(2)  # simulate heavy test
    assert add(2, 3) == 5

def test_multiply():
    time.sleep(2)  # simulate heavy test
    assert multiply(3, 4) == 12
