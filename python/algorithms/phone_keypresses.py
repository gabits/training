"""
Given a phone keyboard, calculate how many keypress does the user have to do in order to construct
the given sentence.
"""

# Challenge 1: Only consider lowercase alphanumeric strings.
PHONE_KEYBOARD = (
    (
        '&1', 'abc2', 'def2',
        'ghi4', 'jkl5', 'mno6',
        'pqrs7', 'tuv8', 'wxyz9',
        '*', ' 0', '#',
     )
)


def how_many_keypresses(phrase: str) -> int:
    sum_of_presses = 0
    for letter in phrase:
        for key_map in PHONE_KEYBOARD:
            if letter in key_map:
                presses_for_key = key_map.index(letter) + 1
                sum_of_presses += presses_for_key
    return sum_of_presses


def test_returns_positive_integer_for_str_word_or_sentence():
    assert how_many_keypresses('foobar') == 15
    assert how_many_keypresses('biz baz') == 17
    assert how_many_keypresses('#calm&serene') == 25


def test_returns_zero_if_string_is_empty():
    assert how_many_keypresses('') == 0


if __name__ == '__main__':
    test_returns_positive_integer_for_str_word_or_sentence()
    test_returns_zero_if_string_is_empty()
