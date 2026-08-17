[![Python application](https://github.com/JorisKaestner/Sudoku_Solver/actions/workflows/python-app.yml/badge.svg)](https://github.com/JorisKaestner/Sudoku_Solver/actions/workflows/python-app.yml)
# Sudoku Solver
Command-line program to solve Sudoku puzzles and verify boards and solutions. Sudokus can be read from file or extracted from screenshots.

## Installation

    git clone https://github.com/JorisKaestner/Sudoku_Solver.git
    cd Sudoku_Solver
    pip install -e ".[dev,ocr]"

Requires Python 3.10+

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

## Prerequisites for OCR features
Pre-trained model can be found at src/sudoku_reader/models. To recreate the models run `python src/sudoku_reader/model_trainer.py`. To load your own model, you have to add your model path in the source code at `src/sudoku_reader/reader.py` for now.

Model accuracy is at >95% per cell. Reading whole puzzles is not reliable, so check the detected input visually.

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
