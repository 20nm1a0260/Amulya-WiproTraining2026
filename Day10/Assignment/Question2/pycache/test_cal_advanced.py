from Calculator import mul, div
import pytest


def test_multiplication(sample_numbers):
    assert mul(sample_numbers[0],sample_numbers[1])==6

def test_division(sample_numbers):
    assert div(sample_numbers[0],sample_numbers[1])==1.5

def test_divisionbyzero(calculator_resource):
    with pytest.raises(ValueError):
        div(10,0)