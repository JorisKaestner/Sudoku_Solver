# Sudoku Solver
Command-line program to solve Sudoku puzzles and verify boards and solutions. Sudokus can be read from file or extracted from screenshots.

!!! Reading puzzles from images is still inaccurate !!!

## Installation

    git clone https://github.com/JorisKaestner/Sudoku_Solver.git
    cd Sudoku_Solver
    pip install -e ".[dev,ocr]"

Requires Python 3.10+

## Prerequisites for OCR features
Pre-trained model can be found at src/sudoku_reader/digit_model.keras. To recreate the model use the   `train_classifier()` method at src/sudoku_reader/digit_classifier.py.

## Usage
### Verify the current state of a Sudoku puzzle
by image:  
`python main.py check --image path/to/sudoku.png [--solved]`

by file:  
`python main.py check --file path/to/sudoku.txt [--solved]`

### Print the solution to a Sudoku puzzle

by image:  
`python main.py solve --image path/to/sudoku.png [--algorithm ALGORITHM]`

by file:  
`python main.py solve --file path/to/sudoku.txt [--algorithm ALGORITHM]`

### Check if Sudoku has at least one valid solution without printing the solution
by image:  
`python main.py solvable --image path/to/sudoku.png [--algorithm ALGORITHM]`

by file:  
`python main.py solvable --file path/to/sudoku.txt [--algorithm ALGORITHM]`

    ALGORITHM: backtracking (default) 

Backtracking is the only solving algorithm yet. 

## Input constraints
Images should be screenshots of Sudokus with the outer borders visible and no extra objects or lines in the image.

Txt files should contain the board line by line, with empty cells as 0s and no extra spaces.  
Example:

    800032000  
    000016789  
    146000002  
    382000090  
    000907810  
    000300426  
    214003900  
    050009631  
    030870000  


## Running tests
    pytest

## Project structure
    src/sudoku/          — board logic, checker, solving algorithms
    src/sudoku_reader/   — OCR pipeline for reading puzzles from images
    test/                — test suite

## License
MIT — see [LICENSE](LICENSE) for details.
