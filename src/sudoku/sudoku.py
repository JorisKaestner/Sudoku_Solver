import numpy as np
class Sudoku:
    def __init__(self, grid):
        try:
            inputType = str(type(grid))
            grid = np.asarray(grid)
        except:
            raise TypeError(f"Array-like type was expected, but {inputType} was provided, when creating the Sudoku.")
        
        if grid.shape != (9,9):
            shape = str(grid.shape)
            raise ValueError(f"9x9 grid was expected, but {shape} dimensions were provided, when creating the Sudoku.")
        self.grid = grid
        return
    
    def getGrid(self):
        return self.grid
        
    def getRow(self, row):
        return self.grid[row, :]

    def getColumn(self, col):
        return self.grid[:, col]
    
    def getBlockNumber(self, row, col):
        return (int(row/3)*3 + int(col//3))

    def getBlock(self, block):
        """Returns block section of the grid as numpy array. The blocks are numbered from 0 to 8 as follows:\n
            0 1 2\n
            3 4 5\n
            6 7 8
        """
        if block < 0 or block > 8:
            raise IndexError(f"Block number can only be between 0 and 8. Block number {block} was provided.")
        x = block*3 % 9
        print(x)
        y = int(block/3)*3
        print(y)
        return self.grid[y:y+3,x:x+3]

    def __str__(self):
        """Returns Sudoku as formatted table. 0 and empty cells get represented as a dot."""
        n = self.grid.shape[0]  # 9
        box = 3
        cell_w = 3

        def h_line(left, mid, right, fill="─"):
            segments = [fill * (cell_w * box) for _ in range(n // box)]
            return left + mid.join(segments) + right

        top = h_line("┌", "┬", "┐")
        mid_thick = h_line("├", "┼", "┤")
        bottom = h_line("└", "┴", "┘")

        lines = [top]
        for r in range(n):
            row_cells = []
            for c in range(n):
                val = self.grid[r, c]
                s = str(val) if val != 0 else "."
                row_cells.append(s.center(cell_w))
            # group into blocks of 3 with │ separators
            blocks = ["".join(row_cells[i:i+box]) for i in range(0, n, box)]
            lines.append("│" + "│".join(blocks) + "│")
            if (r + 1) % box == 0 and r != n - 1:
                lines.append(mid_thick)
        lines.append(bottom)
        return "\n".join(lines)