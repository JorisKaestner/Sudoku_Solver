# main.py
import sys
import argparse
from pathlib import Path
from sudoku.checker import check_state
from sudoku.solver import solve_backtracking
from sudoku.io import read_sudoku_from_txt

ALGORITHMS = {"backtracking"}

def build_parser():
    parser = argparse.ArgumentParser(description="Sudoku solver and checker.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # check command
    parser_check = subparsers.add_parser("check", help="Verify the current state of the puzzle.")
    parser_check.add_argument('--image', type=Path, help="Path to screenshot of Sudoku.")
    parser_check.add_argument('--file', type=Path, help="Path to txt of Sudoku.")
    parser_check.add_argument(
        "--solved",
        action="store_true",
        default=False,
        help="Treat the board as a completed grid (require it to be full).",
    )
    
    # solve command
    parser_solve = subparsers.add_parser("solve", help="Solve the puzzle and print the solution.")
    parser_solve.add_argument("--image", type=Path, help="Path to screenshot of Sudoku.")
    parser_solve.add_argument('--file', type=Path, help="Path to txt of Sudoku.")
    parser_solve.add_argument(
        "--algorithm",
        choices=ALGORITHMS,
        default="backtracking",
        help="Which solving algorithm to use.",
    )

    # solvable command
    parser_solvable = subparsers.add_parser("solvable", help="Check if Sudoku can be solved, without showing the solution.")
    parser_solvable.add_argument("--image", type=Path, help="Path to screenshot of Sudoku.")
    parser_solvable.add_argument('--file', type=Path, help="Path to txt of Sudoku.")
    parser_solvable.add_argument(
        "--algorithm",
        choices=ALGORITHMS,
        default="backtracking",
        help="Which solving algorithm to use.",
    )    

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    # check for image or file
    if args.image and args.file:
        raise SystemExit("Provide either --image or --file, not both.")
    elif args.image:
        print("Loading model...")
        from sudoku_reader.reader import read_sudoku_from_image # heavy load up
        sdk = read_sudoku_from_image(args.image)
    elif args.file:
        sdk = read_sudoku_from_txt(args.file)    
    else:
        raise SystemExit("Provide either --image or --file")

    print("Sudoku was detected as follows:")
    print(sdk)

    ### check current state or solution ###
    if args.command == "check":
        result = check_state(sdk, args.solved)
        print("Sudoku is valid" if result else "Sudoku is invalid")

    ### solve puzzle and print solution (solve) or omit solution (solvable) ###
    if args.command == "solve" or args.command == "solvable":
        if not check_state(sdk, final=False):
            print("Sudoku is invalid and can not be solved.")
        else:
            if args.algorithm == "backtracking":
                solution = solve_backtracking(sdk)
                if not check_state(solution, final=True):
                    print("No solution has been found.")
                else:
                    if args.command == "solvable":
                        print("This Sudoku has at least one valid solution.")
                    else:
                        print("Solution:")
                        print(solution)
            else:
                print(f"No valid algorithm was selected. Available algorithms are {ALGORITHMS}")

if __name__ == '__main__':
    sys.exit(main())