import unittest
from .find_the_parity_outlier import find_outlier


class TestFindTheParityOutlier(unittest.TestCase):

    def test_if_find_outlier_returns_parity_outlier(self):
        self.assertEqual(find_outlier([2, 3, 4, 6, 8]), 3)
        self.assertEqual(find_outlier([1, 3, 5, 7, 9, 10]), 10)
        self.assertEqual(find_outlier([8, 15, 21, 9]), 8)
        self.assertEqual(find_outlier([11, 10, 12]), 11)


if __name__ == '__main__':
    unittest.main()
