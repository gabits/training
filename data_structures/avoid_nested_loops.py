"""Write a program that takes a list A and prints YES if
A contains two equal elements.
"""

def does_unordered_list_have_equal_elements(A: list) -> str:
    equal_elements = False
    n = len(A)
    while equal_elements:
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if (A[i] == A[j]):
                    equal_elements = True
        break
    return 'YES' if equal_elements else 'NO'


def does_ordered_list_have_equal_elements(A: list) -> str:
    equal_elements = False
    n = len(A)
    while equal_elements:
        for i in range(0, n - 2):
            if A[i] == A[i+1]:
                equal_elements = True
        break
    return 'YES' if equal_elements else 'NO'


def test_two_equal_elements_unordered_list_outputs_yes():
    A = [4, 8, 7, 5, 4, 25]
    assert does_unordered_list_have_equal_elements(A) == 'YES'


def test_no_equal_elements_unordered_list_outputs_no():
    A = [4, 8, 7, 5, 25]
    assert does_unordered_list_have_equal_elements(A) == 'NO'


def test_equal_elements_ordered_list_outputs_yes():
    A = [4, 7, 7, 15, 25]
    assert does_ordered_list_have_equal_elements(A) == 'YES'


def test_no_equal_elements_ordered_list_outputs_no():
    A = [4, 7, 9, 15, 25]
    assert does_ordered_list_have_equal_elements(A) == 'NO'


def output_most_frequent_number(A: list) -> int:
    # TODO: UNFINISHED
    """
    Using only one nested loop, find the most frequent number on a list.

    Notes:
    - Use a dictionary to store count for every frequency (downside: stores
    counts which you already know are useless)
    - Compare biggest current frequency in the loop with a list involving
    the next `count + 1` amount of elements, check if they are all equal then
    consider it the next biggest frequency.
    """"
    n = len(A)
    count = 0
    most_frequent_number = None
    for i in range(0, n - 1):
        if sum(A[i:(i + count + 1)]) == A[i] * count:
            most_frequent_number = A[i]
            count += 1
        else:
            if A[i] == A[i + 1]:
                # predict if next number is more frequent
                else:
                    count = 0
    return most_frequent_number


def test_output_most_frequent_number_when_repeated_numbers():
    A = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7]
    assert output_most_frequent_number(A) == 4


def test_output_most_frequent_number_is_most_recent_when_repeated_numbers():
    A = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7]
    assert output_most_frequent_number(A) == 4


def is_there_a_different_number_in_the_list(A: list) -> str:
    is_there_a_different_number = False
    for i in range(0, n - 1):
        is_there_a_different_number = True if A[i] != A[i + 1] else False
    return is_there_a_different_number


def test_returns_true_when_different_element_on_list():
    A = [3, 1, 3, 3, 3]
    assert is_there_a_different_number_in_the_list(A) == True


def test_returns_false_when_all_elements_equal():
    A = [3, 3, 3, 3, 3]
    assert is_there_a_different_number_in_the_list(A) == False


def does_sorted_list_have_distinct_numbers(A: list) -> str:
    return 'YES' if A[i] != A[-1] else 'NO'


def test_sorted_list_outputs_yes_if_has_distinct_numbers():
    A = [1, 1, 1, 1, 2, 2, 2]
    assert does_sorted_list_have_distinct_numbers(A) == 'YES'


def test_sorted_list_outputs_no_if_does_not_have_distinct_numbers():
    A = [1, 1, 1, 1, 1, 1, 1]
    assert does_sorted_list_have_distinct_numbers(A) == 'NO'


if __name__ == '__main__':
    test_two_equal_elements_unordered_list_outputs_yes()
    test_no_equal_elements_unordered_list_outputs_no()
    test_two_equal_elements_ordered_list_outputs_yes()
    test_no_equal_elements_ordered_list_outputs_no()
    test_output_most_frequent_number_when_repeated_numbers()
    test_output_most_frequent_number_is_most_recent_when_repeated_numbers()
    test_returns_true_when_different_element_on_list()
    test_returns_false_when_all_elements_equal()
    test_sorted_list_outputs_yes_if_has_distinct_numbers()
    test_sorted_list_outputs_no_if_does_not_have_distinct_numbers()
