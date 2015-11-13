import os
import sys

import numpy as np

def load_puzzle(filename):
    """
    Loads a ‘Bridges’ puzzle from a file.

    Each line in the file is treated as a row in the puzzle grid. Positive
    single digits are treated as islands, spaces and zeroes are treated as
    empty spaces in the grid, and all other characters are rejected as invalid
    input.

    Args:
        filename: The name of a file containing the puzzle.

    Returns:
        A two-dimensional array of integers (indexed by row, then column)
        representing the puzzle, with positive numbers for islands and zeroes
        for empty spaces.
    """

    try:
        with open(filename, encoding='utf-8') as puzzle_file:

            puzzle = []

            for line in puzzle_file:
                characters = line.rstrip(os.linesep)
                row = [ 0 if c == ' ' else int(c) for c in characters ]
                puzzle.append(row)

            return puzzle

    except ValueError as e:
        sys.exit('Not a valid puzzle file ‘{}’ ({})'.format(filename, e))

    except IOError as e:
        sys.exit('Error reading the puzzle file ‘{}’ ({})'.format(filename, e.strerror))



def is_valid_puzzle(puzzle):
    """
    Checks the validity of a puzzle.

    Takes a two-dimensional matrix of integers, and ensures that it meets the
    following criteria for being a valid ‘Bridges’ puzzle:

    0) Puzzle must have at least one row
    1) Rows of the puzzle grid must be the same length
    2) Between 1 and 8 bridges may terminate at each island
    3) Islands must border empty space (or the board’s edge) on all sides

    Args:
        puzzle: A 2D array of integers.

    Returns:
        True if puzzle is valid, False otherwise
    """

    # Check for emptiness
    if len(puzzle) == 0:
        return False

    # Check for mismatched row lengths
    row_length = len(puzzle[0])
    for row in puzzle:
        if (len(row) != row_length):
            return False

    # Check for validity of numeric values
    for row in puzzle:
        for e in row:
            if not(0 <= e and e <= 8):
                return False

    # Check for adjacent islands
    P = np.array(puzzle)
    for A in (P, P.T):
        # Rows of P.T are equivalent to columns of P
        for row in A:
            for i in range(0, len(row) - 1):
                if row[i] > 0 and row[i + 1] > 0:
                    return False

    return True
