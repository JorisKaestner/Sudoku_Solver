# reader.py
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

def classify_cell(cell: np.ndarray) -> int:
    """Returns digit predicted by classifier"""
    from sudoku_reader.digit_classifier import DigitClassifier
    classifier = DigitClassifier()
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
