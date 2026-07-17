import sys
import numpy as np
from sudoku.sudoku import Sudoku
import sudoku.checker as checker

def main():
    testGrid = np.random.randint(1,9,(9,9))
    sud = Sudoku(testGrid)
    print(sud)
    checker.check_state(sud)

if __name__ == '__main__':
    sys.exit(main())