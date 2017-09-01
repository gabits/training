from unittest import TestCase, main
from nearest_temperature import find_nearest_temperature

class TestFindNearestTemperature(TestCase):

    def test_if_number_already_in_list_returns_same_number(self):
        self.assertEqual(find_nearest_temperature([-4, 0, 3, 9], 3), 3)

    def test_if_number_is_higher_than_max_returns_max(self):
        self.assertEqual(find_nearest_temperature([-9, -3, 2, 34], 89), 34)

    def test_if_number_is_lower_than_min_returns_min(self):
        self.assertEqual(find_nearest_temperature([-20, 5, 10], -51), -20)

    def test_if_equidistant_comparison_returns_only_higher_temperature(self):
        self.assertEqual(find_nearest_temperature([-19, -3, 0, 8, 14], 11), 14)
        self.assertEqual(find_nearest_temperature([-54, 34, 9, 0, -5, 4, 2], 3), 4)

if __name__ == '__main__':
    main()
