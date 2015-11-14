import unittest

from puzzle import Puzzle

class ValidityTestCase(unittest.TestCase):
    """Tests for instantiation of Puzzle."""

    def test_reject_empty_puzzle(self):
        """Is an empty puzzle rejected?"""
        p = []
        with self.assertRaises(ValueError):
            Puzzle(p)

    def test_reject_mismatched_row_lengths(self):
        """Is a puzzle with mismatched row lengths rejected?"""
        p = [[1, 0], [0, 0, 1]]
        with self.assertRaises(ValueError):
            Puzzle(p)

    def test_reject_invalid_numbers(self):
        """Is a puzzle with numbers other than 0–8 rejected?"""
        ps = [ [[9]], [[10]], [[-1]] ]
        for p in ps:
            with self.assertRaises(ValueError):
                Puzzle(p)

    def test_accept_valid_numbers(self):
        """Is a puzzle with only valid numbers accepted?"""
        p = [[1, 0, 2, 0, 3, 0, 4, 0], [0, 5, 0, 6, 0, 7, 0, 8]]
        Puzzle(p)

    def test_reject_horizontally_adjacent_islands(self):
        """Is a puzzle with horizontally-adjacent islands rejected?"""
        ps = [ [[1, 1]], [[0, 0], [1, 1]] ]
        for p in ps:
            with self.assertRaises(ValueError):
                Puzzle(p)

    def test_reject_vertically_adjacent_islands(self):
        """Is a puzzle with vertically-adjacent islands rejected?"""
        ps = [ [[1, 0], [1, 0]], [[0, 0, 0], [0, 1, 0], [0, 1, 0]] ]
        for p in ps:
            with self.assertRaises(ValueError):
                Puzzle(p)

    def test_accept_valid_puzzle(self):
        """Is a valid puzzle accepted?"""
        ps = [ [[1]], [[1, 0]], [[1, 0, 1], [0, 1, 0]] ]
        for p in ps:
            Puzzle(p)


if __name__ == '__main__':
    unittest.main()
