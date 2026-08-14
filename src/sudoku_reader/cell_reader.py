# cell_reader.py
from sudoku_reader.digit_classifier import DigitClassifier
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
    return classifier.classify(cell)
