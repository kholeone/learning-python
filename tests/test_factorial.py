import pytest
from programs import factorial

def test_factorial_variable():
    assert factorial.fact(0) == 1

