import pytest
from sudoku.checker import check_state
from dummy_sudokus import (
    VALID_UNSOLVED,
    INVALID_ROW,
    INVALID_COLUMN,
    INVALID_BOX,
    EMPTY_BOARD,
)

def test_valid_unsolved():
    assert check_state(VALID_UNSOLVED, False) is True

def test_invalid_row_unsolved():
    assert check_state(INVALID_ROW, False) is False

def test_invalid_col_unsolved():
    assert check_state(INVALID_COLUMN) is False

def test_invalid_box_unsolved():
    assert check_state(INVALID_BOX) is False

def test_empty_board():
    assert check_state(EMPTY_BOARD) is True