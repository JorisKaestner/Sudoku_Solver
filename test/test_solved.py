# test cases for completely solved grids
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
    assert check_state(SOLVED_VALID_1, True)

def test_valid_solved_2():
    assert check_state(SOLVED_VALID_2, True)

def test_invalid__row_solved():
    assert not check_state(SOLVED_INVALID_ROW, True)

def test_invalid_col_solved():
    assert not check_state(SOLVED_INVALID_COLUMN, True)

def test_invalid_box_solved():
    assert not check_state(SOLVED_INVALID_BOX, True)

def tes_valid_unsolved():
    assert not check_state(VALID_UNSOLVED, True)

def test_empty_board():
    assert not check_state(EMPTY_BOARD, True)