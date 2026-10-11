import pytest
from main import *

def test_drop_chip():
    assert Connect4.drop_chip(0) is False
    assert Connect4.drop_chip(8) is False