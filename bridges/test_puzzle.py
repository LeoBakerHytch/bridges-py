import unittest

from puzzle import is_valid_puzzle

class ValidityTestCase(unittest.TestCase):
    """Tests for `is_valid_puzzle` in `io.py`."""

    def test_reject_empty_puzzle(self):
        """Is an empty puzzle rejected?"""
        P = []
        self.assertFalse(is_valid_puzzle(P))

if __name__ == '__main__':
    unittest.main()
