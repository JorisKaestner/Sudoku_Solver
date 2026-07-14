import sys
import numpy as np
from Sudoku import Sudoku

def main():
    testGrid = np.arange(81).reshape(9,9)
    sud = Sudoku(testGrid)
    print(testGrid)
    print(str(sud))

if __name__ == '__main__':
    sys.exit(main())