# test_classifier
import pytest
from sudoku_reader.grid_detector import load_image
from sudoku_reader.grid_detector import extract_squares
from sudoku_reader.grid_detector import resize_cells
from sudoku_reader.cell_reader import classify_cell

solutions = [
[8,0,0,0,3,2,0,0,0,
0,0,0,0,1,6,7,8,9,
1,4,6,0,0,0,0,0,2,
3,8,2,0,0,0,0,9,0,
0,0,0,9,0,7,8,1,0,
0,0,0,3,0,0,4,2,6,
2,1,4,0,0,3,9,0,0,
0,5,0,0,0,9,6,3,1,
0,3,0,8,7,0,0,0,0],

[0,9,3,4,2,7,5,0,0,
0,0,7,0,1,5,3,0,0,
0,2,4,6,8,0,0,0,7,
3,0,0,7,6,0,2,1,9,
6,0,0,0,0,0,0,0,0,
0,0,0,1,3,0,0,0,0,
4,0,5,8,0,0,9,2,6,
0,0,1,2,0,6,0,7,3,
0,7,0,0,0,9,8,0,0],

[0,3,0,0,0,0,0,0,0,
0,0,0,1,9,5,0,0,0,
0,0,8,0,0,0,0,6,0,
8,0,0,0,6,0,0,0,0,
4,0,0,8,0,0,0,0,1,
0,0,0,0,2,0,0,0,0,
0,6,0,0,0,0,2,8,0,
0,0,0,4,1,9,0,0,5,
0,0,0,0,0,0,0,7,0],

[7,1,0,8,2,0,5,0,3,
0,0,0,1,5,4,8,2,7,
0,5,0,0,7,9,0,4,6,
6,7,0,9,0,0,3,0,0,
1,0,2,0,3,0,0,7,0,
9,8,0,0,6,0,4,0,0,
0,0,0,0,0,5,0,3,1,
0,0,0,6,0,0,0,5,0,
5,0,0,7,0,3,2,6,4],

[0,0,0,0,9,5,3,0,0,
5,0,0,0,0,0,6,2,0,
3,0,4,0,0,0,0,0,0,
0,0,0,8,4,0,0,0,0,
0,0,0,3,0,0,0,8,0,
4,6,0,0,0,0,0,0,7,
0,0,0,0,8,7,0,0,6,
7,0,0,0,0,0,9,0,1,
0,5,1,0,0,0,0,0,0]]

def test_check_empty():
    img = load_image("test/sudoku_screenshots/sudoku_0.png")
    empty_cells = resize_cells(extract_squares(img))
    predictions = []
    for cell in empty_cells:
        predictions.append(classify_cell(cell))
    assert any(predictions) == False    # any() returns True for any value other than 0

def test_full_grids():
    for i in range(1,6):
        img = load_image(f"test/sudoku_screenshots/sudoku_{i}.png")
        cells = resize_cells(extract_squares(img))
        predictions = []
        for cell in cells:
            predictions.append(classify_cell(cell))
        assert predictions == solutions[i-1]

