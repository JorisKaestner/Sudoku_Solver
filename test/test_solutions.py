import pytest
from sudoku.checker import check_state
from sudoku.solver import solve_backtracking
from dummy_sudokus import (
    VALID_UNSOLVED,
    EMPTY_BOARD
)

ALGORITHMS = [solve_backtracking]

@pytest.mark.parametrize("solve", ALGORITHMS, ids=lambda f: f.__name__)
def test_unsolvable_empty(solve):
    solution = solve(EMPTY_BOARD)
    assert solution.isEmpty()

@pytest.mark.parametrize("solve", ALGORITHMS, ids=lambda f: f.__name__)
def test_valid_unsolved(solve):
    solution = solve(VALID_UNSOLVED)
    assert check_state(solution, final=True)