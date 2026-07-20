import pytest
from sudoku.checker import check_state
from dummy_sudokus import (
    SOLVED_VALID_1,
    SOLVED_VALID_2,
    SOLVED_INVALID_ROW,
    SOLVED_INVALID_BOX,
    SOLVED_INVALID_COLUMN,
    VALID_UNSOLVED,
    EMPTY_BOARD,
)

def test_valid_solved_1():
    assert check_state(SOLVED_VALID_1, True) is True

def test_valid_solved_2():
    assert check_state(SOLVED_VALID_2, True) is True

def test_invalid__row_solved():
    assert check_state(SOLVED_INVALID_ROW, True) is False

def test_invalid_col_solved():
    assert check_state(SOLVED_INVALID_COLUMN, True) is False

def test_invalid_box_solved():
    assert check_state(SOLVED_INVALID_BOX, True) is False

def tes_valid_unsolved():
    assert check_state(VALID_UNSOLVED, True) is False

def test_empty_board():
    assert check_state(EMPTY_BOARD, True) is False