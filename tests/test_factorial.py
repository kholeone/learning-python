import pytest
from programs import factorial

def test_factorial_1():
    assert factorial.fact(0) == 1

def test_factorial_2():
    assert factorial.fact(3) == 6

