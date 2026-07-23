# test cases for solutions produced by solving algorithms
import pytest
from sudoku.checker import check_state
from sudoku.solver import solve_backtracking
from dummy_sudokus import (
    VALID_START_1,
    VALID_UNSOLVED,
    EMPTY_BOARD
)

SUDOKUS = [VALID_UNSOLVED, VALID_START_1]
ALGORITHMS = [solve_backtracking]

@pytest.mark.parametrize("solve", ALGORITHMS, ids=lambda f: f.__name__)
def test_unsolvable_empty(solve):
    solution = solve(EMPTY_BOARD)
    assert solution.isEmpty()

@pytest.mark.parametrize("solve", ALGORITHMS, ids=lambda f: f.__name__)
@pytest.mark.parametrize("sudokus", SUDOKUS, ids=lambda p: p.name)
def test_solver_produces_valid_solution(sudokus, solve):
    solution = solve(sudokus)
    assert check_state(solution, True)