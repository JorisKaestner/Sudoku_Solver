# cell_reader.py
from sudoku_reader.digit_classifier import DigitClassifier
from sudoku_reader.image_preprocessing import preprocess_cell
from sudoku_reader.grid_detector import load_image
from sudoku_reader.grid_detector import extract_squares
from sudoku.sudoku import Sudoku
import numpy as np

def is_empty_cell(cell: np.ndarray, threshold: float = 0.02) -> bool:
    """Returns true, if sum of dark pixels in image is below threshold percentage"""
    dark_pixels = np.sum(cell < 128)  # sum of all pixels below 128 grayscale value
    dark_fraction = dark_pixels / cell.size
    return dark_fraction < threshold

def classify_cell(cell: np.ndarray, classifier: DigitClassifier = DigitClassifier()) -> int:
    """Returns digit predicted by classifier"""
    if (is_empty_cell(cell)):
        return 0
    prep_cell = preprocess_cell(cell)
    return classifier.classify(prep_cell)

def read_sudoku_from_image(image_path:str) -> Sudoku:
    """Detects grid in the provided image and converts it to a Sudoku object"""
    image = load_image(image_path)
    cells = extract_squares(image)
    predictions = [classify_cell(cell) for cell in cells]
    grid = np.reshape(predictions, (9, 9))
    return Sudoku(grid)

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