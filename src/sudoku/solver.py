from sudoku.sudoku import Sudoku
import copy

def solve_backtracking(sdk: Sudoku) -> Sudoku:
    if sdk.isEmpty():
        print("Sudoku is empty and cannot be solved.")
        return Sudoku([[0] * 9 for _ in range(9)])
    
    working_sdk = copy.deepcopy(sdk)
    return working_sdk