# test cases for unsolved (starting grid) sudokus
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
    assert check_state(VALID_UNSOLVED, False)

def test_invalid_row_unsolved():
    assert not check_state(INVALID_ROW, False)

def test_invalid_col_unsolved():
    assert not check_state(INVALID_COLUMN)

def test_invalid_box_unsolved():
    assert not check_state(INVALID_BOX)

def test_empty_board():
    assert check_state(EMPTY_BOARD)