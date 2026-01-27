
import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def test_add():
    assert add(2,3)==5

def test_sub():
    assert subtract(5,4)==1

def test_mutliply():
    assert multiply(4,5)==20

def test_divide():
    assert divide(20,4)==5

def test_divisionbyzero():
    with pytest.raises(ValueError):
        divide(10,0)
