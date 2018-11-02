def find_nearest_temperature(temperatures, number):
    if number in temperatures:
        return number
    elif number > max(temperatures):
        return max(temperatures)
    elif number < min(temperatures):
        return min(temperatures)
    else:
        temperatures.sort()
        for index in range(len(temperatures)):
            if number > temperatures[index]:
                pass
            else:
                avg_comparison = (temperatures[index] + temperatures[index - 1]) / 2
                if number == avg_comparison or number > avg_comparison:
                    return temperatures[index]
                else:
                    return temperatures[index - 1]


def test_if_number_already_in_list_returns_same_number(self):
    assert find_nearest_temperature([-4, 0, 3, 9], 3) == 3

def test_if_number_is_higher_than_max_returns_max(self):
    assert find_nearest_temperature([-9, -3, 2, 34], 89) == 34

def test_if_number_is_lower_than_min_returns_min(self):
    assert find_nearest_temperature([-20, 5, 10], -51) == -20

def test_if_equidistant_comparison_returns_only_higher_temperature(self):
    assert find_nearest_temperature([-19, -3, 0, 8, 14], 11) == 14
    assert find_nearest_temperature([-54, 34, 9, 0, -5, 4, 2], 3) == 4


if __name__ == '__main__':
    test_if_number_already_in_list_returns_same_number()
    test_if_number_is_higher_than_max_returns_max()
    test_if_number_is_lower_than_min_returns_min()
    test_if_equidistant_comparison_returns_only_higher_temperature()
