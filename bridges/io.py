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
            pass

    except FileNotFoundError as e:
        sys.exit('Could not find the puzzle file ‘{}’'.format(filename))

    except IOError as e:
        sys.exit('Error reading the puzzle file ‘{}’'.format(filename))
