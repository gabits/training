"""
Your job is to write a function which increments a string to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number the number 1 should be appended to the new string.

Examples:
    - foo -> foo1
    - foobar23 -> foobar24
    - foo0042 -> foo0043
    - foo9 -> foo10
    - foo099 -> foo100

Attention:
    If the number has leading zeros the amount of digits should be considered.

"""


# NOTE: check if solving with a list is more readable or optmised

def increment_number_with_leading_zeroes(numbers_with_leading_zeroes: str) -> str:
    incremented_number = str(int(numbers_with_leading_zeroes) + 1)
    # Handle leading zeroes if any
    difference_in_length = len(numbers_with_leading_zeroes) - len(incremented_number)
    if difference_in_length > 0:
        incremented_number = '0' * difference_in_length + incremented_number

    # Replace the original number by the new one
    return incremented_number


def increment_string_via_string_method(string: str) -> str:
    """
    Increments the given string by the integer 1, either appending it to the last non-numerical
    character, or by summing it up to the number formed by the last integer characters.
    """
    # Builds a string with all numbers in the end of the string if any, in reverse order, then
    # sums 1 to it and replaces the original number in the string, accounting for any original
    # leading zeroes.
    ending_numbers: str = ''
    for char in string[::-1]:
        if char in '0123456789':
            ending_numbers += char
        else:
            break
    if ending_numbers:
        ending_numbers: str = ending_numbers[::-1]
        new_number = increment_number_with_leading_zeroes(ending_numbers)
        modified_string = string.replace(ending_numbers, str(new_number))
    else:
        modified_string = string + '1'
    return modified_string


def test_string_incremented_ends_in_1_if_last_character_not_an_integer():
    assert increment_string_via_string_method('foobar099') == 'foobar100'
    assert increment_string_via_string_method('foobar0042') == 'foobar0043'
    assert increment_string_via_string_method('12foobar1234') == '12foobar1235'
    assert increment_string_via_string_method('1foo5bar9') == '1foo5bar10'


def test_string_increments_number_by_1_if_last_character_is_an_integer():
    assert increment_string_via_string_method('foobar') == 'foobar1'
    assert increment_string_via_string_method('foo123bar') == 'foo123bar1'
    assert increment_string_via_string_method('3244foobar') == '3244foobar1'


if __name__ == '__main__':
    test_string_incremented_ends_in_1_if_last_character_not_an_integer()
    test_string_increments_number_by_1_if_last_character_is_an_integer()
    print("All tests pass!")
