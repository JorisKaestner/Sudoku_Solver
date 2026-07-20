import sys
import numpy as np
from sudoku.sudoku import Sudoku
import sudoku.checker as checker

def main():
    sud = Sudoku([[0] * 9 for _ in range(9)])
    print(sud.isEmpty())

if __name__ == '__main__':
    sys.exit(main())