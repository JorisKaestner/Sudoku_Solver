# test cases for appropriate grid detection from images
import pytest
from pathlib import Path
from sudoku_reader.grid_detector import load_image
from sudoku_reader.grid_detector import detect_edges
from sudoku_reader.grid_detector import detect_lines
from sudoku_reader.grid_detector import merge_nearest_lines
from sudoku_reader.grid_detector import extract_squares
from sudoku_reader.grid_detector import resize_cells

SUDOKU_DIR = Path("test/sudoku_screenshots")
SUDOKU_PATHS = sorted(SUDOKU_DIR.glob("sudoku_*"))

@pytest.mark.parametrize("path", SUDOKU_PATHS, ids=lambda p: p.stem)
def test_count_detected_squares(path):
    sudoku = load_image(str(path))
    squares = extract_squares(sudoku)
    assert len(squares) == 81

@pytest.mark.parametrize("path", SUDOKU_PATHS, ids=lambda p: p.stem)
def test_count_detected_lines(path):
    sudoku = load_image(str(path))
    hor_lines, ver_lines = merge_nearest_lines(detect_lines(detect_edges(sudoku)))
    assert len(hor_lines) == 8 and len(ver_lines) == 8

@pytest.mark.parametrize("path", SUDOKU_PATHS, ids=lambda p: p.stem)
def test_resize_cells(path):
    sudoku = load_image(str(path))
    cells = resize_cells(extract_squares(sudoku))
    for cell in cells:
        assert cell.shape == (28, 28)
