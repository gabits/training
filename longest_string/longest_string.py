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


print(generate_longest_consecutive_string(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 2))