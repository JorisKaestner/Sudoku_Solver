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

def crop_to_content(cell: np.ndarray, border_trim: int = 10) -> np.ndarray:
    """Trim a fixed border margin first (removes thin grid-line fragments),
    then tightly crop to the digit's actual bounding box."""
    h, w = cell.shape
    trimmed = cell[border_trim:h-border_trim, border_trim:w-border_trim]

    _, thresh = cv2.threshold(trimmed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    coords = cv2.findNonZero(thresh)

    if coords is None:
        return trimmed  # empty cell, nothing to crop to

    x, y, w2, h2 = cv2.boundingRect(coords)
    return trimmed[y:y+h2, x:x+w2]

def binarize_and_invert(cell: np.ndarray) -> np.ndarray:
    _, binary = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def preprocess_cell(cell: np.array) -> np.array:
    img_pipe = resize_cell(cell)
    #img_pipe = center_digit(img_pipe)
    img_pipe = binarize_and_invert(img_pipe)
    return img_pipe