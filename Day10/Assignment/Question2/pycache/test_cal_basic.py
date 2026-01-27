
from Calculator import add, sub
import pytest

def setup_module(module):
    print("\n setup before module")

def teardown_module(module):
    print("\n teardown after module")

def setup_function(function):
    print("\n setup before function")

def teardown_function(function):
    print("\n teardown after function")

def test_addition(sample_numbers):
    assert add(sample_numbers[0],sample_numbers[1])==5

def test_subtraction(sample_numbers):
    assert sub(sample_numbers[0],sample_numbers[1])==1

    
