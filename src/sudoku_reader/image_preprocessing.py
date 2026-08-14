# image_preprocessing
import numpy as np
import cv2

def resize_cell(cell:np.array, cell_size:int=28) -> np.array:
    """Resize image to a fixed length and width and returns as new image.\n
    Preprocessing and normalisation step for mnist classification."""
    return cv2.resize(cell, (cell_size, cell_size), interpolation=cv2.INTER_AREA)

def invert_cell(cell:np.array) -> np.array:
    """Inverts image.\n
    Preprocessing and normalisation step for mnist classification."""
    return 255 - cell

def center_digit(cell: np.ndarray) -> np.ndarray:
    """Calculates center of mass for cell.\n
    Preprocessing and normalisation step for mnist classification."""
    moments = cv2.moments(cell)
    if moments["m00"] == 0:
        return cell  # avoid divide-by-zero on a near-empty cell
    cx = moments["m10"] / moments["m00"]
    cy = moments["m01"] / moments["m00"]
    h, w = cell.shape
    shift_x, shift_y = w // 2 - cx, h // 2 - cy
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    return cv2.warpAffine(cell, M, (w, h))