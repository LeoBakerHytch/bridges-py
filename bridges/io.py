import os
import sys

def load_puzzle(filename):
    """
    Loads a ‘Bridges’ puzzle from a file.

    Each line in the file is treated as a row in the puzzle grid. Positive
    digits are treated as islands, spaces and zeroes are treated as empty spaces
    in the grid, and all other characters are rejected as invalid input.

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

    * Between 1 and 8 bridges may terminate at each island
    * Rows of the puzzle grid must be the same length
    * Islands must border empty space (or the board’s edge) on all sides

    Args:
        puzzle: A 2D array of integers.

    Returns:
        True if puzzle is valid, False otherwise
    """

    return True
