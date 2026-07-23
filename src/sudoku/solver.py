# sudoku solving algorithms
from sudoku.sudoku import Sudoku
from sudoku.checker import check_placement
import copy

def solve_backtracking(sdk: Sudoku) -> Sudoku:
    if sdk.isEmpty():
        print("Sudoku is empty and cannot be solved.")
        return Sudoku([[0] * 9 for _ in range(9)])
    working_sudoku = copy.deepcopy(sdk)
    solve_backtracking_rec(working_sudoku, 0, 0)

    return working_sudoku

def solve_backtracking_rec(sdk, row, col):
    grid = sdk.getGrid()
    # base case
    if row==8 and col == 9:
        return True

    # skip to next row after last coloumn
    if col == 9:
        row += 1
        col = 0

    # skip cell if not empty
    if grid[row][col] != 0:
        return solve_backtracking_rec(sdk, row, col+1)

    ## recursive call ##
    # - try to place digit and call function recursively for the next cell (depth-first)
    # - function will backtrack if approach failed and try next digit
    # - base case is reached at the end of the grid
    for digit in range(1,10):
        if check_placement(sdk, digit, row, col):
            grid[row][col] = digit
            if solve_backtracking_rec(sdk, row, col+1):
                return True
            grid[row][col] = 0 # reset cell if current approach failed

    return False
