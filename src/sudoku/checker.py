from sudoku.sudoku import Sudoku

def check_state(state, final=False):
    """Returns true, if there are no duplicate digits in rows, coloumns or blocks
    in the current state and false otherwise.
    Returns false, if the solution is final and has empty cells.
    DOES NOT CHECK FOR SOLVABILITY."""

    rows = [[0] * 10 for _ in range(10)]
    cols = [[0] * 10 for _ in range(10)]
    blocks = [[0] * 10 for _ in range(10)]

    grid = state.getGrid()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # skip empty cells or return false if final
            if grid[row][col] == 0:
                if final:
                    print(f"Sudoku has not been completed. Empty cell at {row},{col}")
                    return False
                else:
                    continue
            
            try:
                digit = grid[row][col]

                # check rows for duplicates
                if rows[row][digit] == 0:
                    rows[row][digit] = 1
                else:
                    print(f"Duplicate digit {digit} at {row}, {col}")
                    return False
                
                # check coloumns for duplicates
                if cols[col][digit] == 0:
                    cols[col][digit] = 1
                else:
                    print(f"Duplicate digit {digit} at {row}, {col}")
                    return False
                
                # check blocks for duplicates
                blockNumber = state.getBlockNumber(row, col)
                if blocks[blockNumber][digit] == 0:
                    blocks[blockNumber][digit] = 1
                else:
                    print(f"Duplicate digit {digit} in block {blockNumber}")
                    return False
            
            # check for invalid digits
            except IndexError:
                print(f"Invalid digit {grid[row][col]} at {row},{col}")
                return False
    if final:
        print("Solution was verified.")
        return True
    else:
        print("Current state is valid.")
        return True
