import unittest

from puzzle import is_valid_puzzle

class ValidityTestCase(unittest.TestCase):
    """Tests for `is_valid_puzzle` in `io.py`."""

    def test_reject_empty_puzzle(self):
        """Is an empty puzzle rejected?"""
        P = []
        self.assertFalse(is_valid_puzzle(P))

    def test_reject_mismatched_row_lengths(self):
        """Is a puzzle with mismatched row lengths rejected?"""
        P = [[1, 0], [0, 0, 1]]
        self.assertFalse(is_valid_puzzle(P))

    def test_reject_invalid_numbers(self):
        """Is a puzzle with numbers other than 0–8 rejected?"""
        Ps = [ [[9]], [[10]], [[-1]] ]
        for P in Ps:
            self.assertFalse(is_valid_puzzle(P))

    def test_reject_horizontally_adjacent_islands(self):
        """Is a puzzle with horizontally-adjacent islands rejected?"""
        Ps = [ [[1, 1]], [[0, 0], [1, 1]] ]
        for P in Ps:
            self.assertFalse(is_valid_puzzle(P))

    def test_reject_vertically_adjacent_islands(self):
        """Is a puzzle with vertically-adjacent islands rejected?"""
        Ps = [ [[1, 0], [1, 0]], [[0, 0, 0], [0, 1, 0], [0, 1, 0]] ]
        for P in Ps:
            self.assertFalse(is_valid_puzzle(P))


if __name__ == '__main__':
    unittest.main()
