import pytest
from programs import list_of_squares

def test_list_of_squares_1():
    assert list_of_squares.list_of_squares(0) == {}

def test_list_of_squares_2():
    assert list_of_squares.list_of_squares(2) == {1: 1, 2: 4}