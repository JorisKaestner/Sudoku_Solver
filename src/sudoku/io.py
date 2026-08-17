# io.py
from sudoku.sudoku import Sudoku

def read_sudoku_from_txt(file_path:str) -> Sudoku:
    """Reads Sudoku from a plain text file. Example file is shown below:\n
    800032000\n
    000016789\n
    146000002\n
    382000090\n
    000907810\n
    000300426\n
    214003900\n
    050009631\n
    030870000
    """
    lines = [line.strip() for line in file_path.read_text().splitlines() if line.strip()]

    if len(lines) != 9:
        raise ValueError(f"Expected 9 rows, got {len(lines)}")

    grid = []
    for row_num, line in enumerate(lines):
        if len(line) != 9:
            raise ValueError(f"Row {row_num} has {len(line)} characters, expected 9: '{line}'")
        if not line.isdigit():
            raise ValueError(f"Row {row_num} contains non-digit characters: '{line}'")
        grid.append([int(ch) for ch in line])

    return Sudoku(grid)
