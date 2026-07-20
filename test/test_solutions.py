import pytest
from sudoku.checker import check_state
from sudoku.solver import solve_sudoku
from dummy_sudokus import (
    EMPTY_BOARD
)

def test_unsolvable_empty():
    assert solve_sudoku(EMPTY_BOARD).isEmpty() is True