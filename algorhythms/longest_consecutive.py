"""
You are given an array strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"g

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""
#
# Attempt 1
#
def generate_longest_consecutive_string(strarr, k):
    longest_consecutive = ''
    if len(strarr) != 0 and k < len(strarr) and k > 0:
        lenghts_list = []
        for index in range(len(strarr) - k):
            number = 0
            for string in strarr[index:(index + k)]:
                count += len(string)
            lenghts_list.append(count)
        starting_index = lenghts_list.index(max(lenghts_list))
        longest_consecutive = "".join(strarr[starting_index:(starting_index + k)])
    return longest_consecutive

#
# Attempt 2
#
def _remove_duplicates(list_of_strings):
    # Step 1: Remove all list duplicates, if any, maintaining the first instance of the string
    list_of_strings.reverse()
    for string in list_of_strings:
        while list_of_strings.count(string) > 1:
            list_of_strings.remove(string)
    list_of_strings.reverse()
    return

def _get_longest_str(list_of_strings):
    # Step 2: Find all relevant elements in list (longest strings)
    longest_string = list_of_strings[0]
    if len(list_of_strings) > 1:
        for i in range(1, len(list_of_strings)):
            if len(list_of_strings[i]) > len(list_of_strings[i - 1]):
                longest_string = list_of_strings[i]
    list_of_strings.remove(longest_string)
    return longest_string

def _get_relevant_strings(list_of_strings, k):
    # Step 3: Get the k longest strings of the list
    relevant_strings = []
    while k > 0:
        longest_string = _get_longest_str(list_of_strings)
        relevant_strings.append(longest_string)
        k -= 1
    return relevant_strings

def generate_longest_consecutive_string(strarr, k):
    # Step 4: Append the relevant strings together in order
    longest_consecutive_string = ''
    _remove_duplicates(strarr)
    list_of_strings = strarr.copy()
    if len(list_of_strings) > 0 and k < len(list_of_strings) and k > 0:
        relevant_strings = _get_relevant_strings(list_of_strings, k)
        for string in strarr:
            if string in relevant_strings:
                longest_consecutive_string += string
    return longest_consecutive_string

#
#   Tests
#
def test_expected_results(self):
    assert generate_longest_consecutive_string(
        ["zone", "abigail", "theta", "form", "libe", "zas"], 2
    ) == "abigailtheta"
    assert generate_longest_consecutive_string(
        ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1
    ) == "oocccffuucccjjjkkkjyyyeehh"
    assert generate_longest_consecutive_string([], 3) == ""
    assert generate_longest_consecutive_string(
        ["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2
    ) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
    assert generate_longest_consecutive_string(
        ["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2
    ) == "wlwsasphmxxowiaxujylentrklctozmymu"
    assert generate_longest_consecutive_string(
        ["zone", "abigail", "theta", "form", "libe", "zas"], -2
    ) == ""
    assert generate_longest_consecutive_string(
        ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3
    ) == "ixoyx3452zzzzzzzzzzzz"
    assert generate_longest_consecutive_string(
        ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15
    ) == ""
    assert generate_longest_consecutive_string(
        ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0
    ) == ""
