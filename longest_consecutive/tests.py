from unittest import TestCase
from .longest_consecutive import generate_longest_consecutive_string


class TestLongestStrings(TestCase):

    def test_expected_results(self):
        self.assertEqual(generate_longest_consecutive_string(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(generate_longest_consecutive_string(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(generate_longest_consecutive_string([], 3), "")
        self.assertEqual(generate_longest_consecutive_string(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(generate_longest_consecutive_string(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(generate_longest_consecutive_string(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(generate_longest_consecutive_string(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(generate_longest_consecutive_string(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEqual(generate_longest_consecutive_string(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
