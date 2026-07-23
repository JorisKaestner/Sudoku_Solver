import numpy as np
class Sudoku:
    def __init__(self, grid):
        # convert grid to np array if possible
        try:
            inputType = str(type(grid))
            grid = np.asarray(grid)
        except:
            raise TypeError(f"Array-like type was expected, but {inputType} was provided, when creating the Sudoku.")
        
        # check grid shape
        if grid.shape != (9,9):
            shape = str(grid.shape)
            raise ValueError(f"9x9 grid was expected, but {shape} dimensions were provided, when creating the Sudoku.")
        self.grid = grid
        return
    
    def getGrid(self) -> np.array:
        return self.grid
        
    def getRow(self, row: int) -> np.array:
        return self.grid[row, :]

    def getColumn(self, col: int) -> np.array:
        return self.grid[:, col]
    
    def getBlockIndex(self, row: int, col: int) -> int:
        """Returns the ID of the block, the specified cell is situated in. 
        The blocks are numbered from 0 to 8 as follows:\n
            0 1 2\n
            3 4 5\n
            6 7 8
        """
        return (int(row/3)*3 + int(col//3))

    def getBlock(self, blockID: int) -> np.array:
        """Returns block section of the grid as numpy array. The blocks are numbered from 0 to 8 as follows:\n
            0 1 2\n
            3 4 5\n
            6 7 8
        """
        if blockID < 0 or blockID > 8:
            raise IndexError(f"Block number can only be between 0 and 8. Block number {blockID} was provided.")
        x = blockID*3 % 9
        y = int(blockID/3)*3
        return self.grid[y:y+3,x:x+3]
    
    def isEmpty(self) -> bool:
        return bool(np.count_nonzero(self.grid) == 0)

    def __str__(self) -> str:
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