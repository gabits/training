# import unittest


def find_outlier(integers):
    for o in integers:
        copied_list = integers.copy()
        copied_list.remove(o)
        if o % 2 != (copied_list[0] % 2) and (o % 2) != (copied_list[1] % 2):
            return o


# class TestFindOutlier(unittest.TestCase):
#
#     def test_if_find_outlier_returns_different_number(self):
#         self.assertEqual(find_outlier([2, 6, 8, 10, 3]), 3)
#
#
# unittest.main()


find_outlier([2, 6, 8, 10, 3])