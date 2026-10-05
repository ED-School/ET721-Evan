"""
Evan Dong
Oct 5, 2026
lab 9: unit testing using Pytest
"""

import pytest

from math_utils import *

def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(-1,5) == 5

def test_divide():
    assert divide(10,2) == 5
    assert divide(10,3) == pytest.approx(0.33, abs=0.01)