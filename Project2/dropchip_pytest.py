
import pytest
from main import Connect4

@pytest.fixture
def game():
    return Connect4()

# Test valid drop chip
def test_successful_drop(game):
    assert game.drop_chip(1) is True

# test Full Columns
def test_full_column(game):
    for _ in range(game.ROWS):
        game.drop_chip(1)
    assert game.drop_chip(1) is False

# Test Invalid Columns
@pytest.mark.parametrize("column", [0, -1, Connect4.COLS + 1, 100])
def test_invalid_column(game,column):
    assert game.drop_chip(column) is False

# Test Full Board

def test_full_board():
    game = Connect4()
    for col in range(1, Connect4.COLS + 1):
        for _ in range(Connect4.ROWS):
            assert game.drop_chip(col) is True
            game.switch_player()

    assert game.is_full() is True
    for col in range(1, Connect4.COLS + 1):
        assert game.drop_chip(col) is False

# For some reason the final test for full board didn't appear so I had to ask AI to help reconfigure it
# Had a hard time understanding the main.py so I asked AI to help me along the process
# When starting out, my first two tests for the valid drop chip and full column created an error, but somehow also the first test passed so I asked AI for help
# when runned you should get a total of 7 passed tests with four of them being related to the invalid column test to see how far the range is