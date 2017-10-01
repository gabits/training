import unittest
from .sum_consecutive_equal_integers import sum_consecutive_integers


class TestSumConsecutiveEqualsIntegers(unittest.TestCase):
    def test_if_sum_consecutives_returns_sum_of_consecutive_integers(self):
        self.assertEqual(sum_consecutive_integers([1, 4, 4, 4, 0, 4, 3, 3, 1]), [1, 12, 0, 4, 6, 1])
        self.assertEqual(sum_consecutive_integers([1, 1, 7, 7, 3]), [2, 14, 3])
        self.assertEqual(sum_consecutive_integers([-5, -5, 7, 7, 12, 0]), [-10, 14, 12, 0])
        self.assertEqual(sum_consecutive_integers([3, 3, 3, 3, 1]), [12, 1])


if __name__ == '__main__':
    unittest.main()
