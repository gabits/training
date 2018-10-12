"""You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns N.


For example:

    [2, 4, 0, 100, 4, 11, 2602, 36]
    Should return: 11

    [160, 3, 1719, 19, 11, 13, -21]
    Should return: 160

"""


def find_outlier(integers):
    for o in integers:
        copied_list = integers.copy()
        copied_list.remove(o)
        if o % 2 != (copied_list[0] % 2) and (o % 2) != (copied_list[1] % 2):
            return o


def test_if_find_outlier_returns_parity_outlier(self):
    assert find_outlier([2, 3, 4, 6, 8]) == 3
    assert find_outlier([1, 3, 5, 7, 9, 10]) == 10
    assert find_outlier([8, 15, 21, 9]) == 8
    assert find_outlier([11, 10, 12]) == 11
