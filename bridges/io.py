import sys

def load_puzzle(filename):
    """
    Loads and validates a ‘Bridges’ puzzle from a file

    Args:
        filename: The name of a file containing the puzzle

    Returns:
        A two-dimensional array of integers (indexed by row, then column)
        representing the puzzle, with positive numbers for islands and zeroes
        for empty spaces
    """

    try:
        with open(filename, encoding='utf-8') as puzzle_file:
            pass

    except FileNotFoundError as e:
        sys.exit('Could not find the puzzle file ‘{}’'.format(filename))

    except IOError as e:
        sys.exit('Error reading the puzzle file ‘{}’'.format(filename))
