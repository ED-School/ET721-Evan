"""
Evan Dong
Oct 5, 2026
lab 9: unit testing using Pytest
"""

import pytest

from math_utils import *

def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(1,5) == 5

def test_divide():
    assert divide(10,2) == 5
    assert divide(10,3) == pytest.approx(3.33, abs=0.01)

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10,0)

# exercise 2
def test_valid_password():
    assert validate_password("pass12345") is True

def test_short_password():
    assert validate_password("pass1") is False

def test_no_number():
    assert validate_password("testingpassword") is False

# execrise 3
# use parametrize to set multiple testing input/output sets
@pytest.mark.parametrize(
    "n, excepted", [(2, True), (3, False), (0, False), (-2, True), (7, False)]
)

def test_is_even(n,excepted):
    assert is_even(n) == excepted

# execrise 4
@pytest.mark.parametrize(
    "n, expected",
    [
        ("oofergod69", True),
        ("Letmein", False),
        ("Can1", False),
    ]
)
def test_password(n,expected):
    assert validate_password(n) == expected