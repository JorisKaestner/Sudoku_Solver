# test cases for solutions produced by solving algorithms
import pytest
from sudoku.checker import check_state
from sudoku.solver import solve_backtracking
from dummy_sudokus import (
    VALID_START_1,
    VALID_UNSOLVED,
    EMPTY_BOARD
)

ALGORITHMS = [solve_backtracking]

@pytest.mark.parametrize("solve", ALGORITHMS, ids=lambda f: f.__name__)
def test_unsolvable_empty(solve):
    solution = solve(EMPTY_BOARD)
    assert solution.isEmpty()

@pytest.mark.parametrize("solve", ALGORITHMS, ids=lambda f: f.__name__)
def test_valid_solution_easy(solve):
    solution = solve(VALID_START_1)
    assert check_state(solution, True)