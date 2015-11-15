import os
import numpy as np

class Puzzle:

    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.validate()


    @classmethod
    def from_file(cls, filename):
        """
        Instantiates a new Puzzle with data from a file.

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

        matrix = []

        try:
            with open(filename, encoding='utf-8') as puzzle_file:

                try:
                    for line in puzzle_file:
                        characters = line.rstrip(os.linesep)
                        row = [ 0 if c == ' ' else int(c) for c in characters ]
                        matrix.append(row)

                except ValueError as e:
                    raise Error('Puzzle file contains invalid characters') from e

        except IOError as e:
            raise Error('Could not read the puzzle file ‘{}’'.format(filename)) from e

        return cls(matrix)


    def validate(self):
        """
        Checks the validity of the puzzle matrix.

        Ensures that the puzzle matrix meets the following criteria for being a
        valid ‘Bridges’ puzzle:

        0) The puzzle must have at least one row
        1) Puzzle rows must be the same length
        2) Between 1 and 8 bridges may terminate at each island
        3) Islands must border empty space (or the board’s edge) on all sides

        Raises:
            ValueError: if any of the constraints are not met.
        """

        # Check for emptiness
        if len(self.matrix) == 0:
            raise ValueError('Puzzle contains no rows')

        # Check for mismatched row lengths
        row_length = len(self.matrix[0])
        for row in self.matrix:
            if (len(row) != row_length):
                raise ValueError('Puzzle rows not all of same length')

        # Check for validity of numeric values
        for e in self.matrix.flat:
            if not(0 <= e and e <= 8):
                raise ValueError('Puzzle contains invalid value: {}'.format(e))

        # Check for adjacent islands
        for M in (self.matrix, self.matrix.T):
            # Rows of matrix transpose are equivalent to columns of matrix
            for row in M:
                for i in range(0, len(row) - 1):
                    if row[i] > 0 and row[i + 1] > 0:
                        raise ValueError('Puzzle contains adjacent islands')
