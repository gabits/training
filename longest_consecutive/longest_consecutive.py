def generate_longest_consecutive_string(strarr, k):
    longest_consecutive = ''
    if len(strarr) != 0 and k < len(strarr) and k > 0:
        lenghts_list = []
        for index in range(len(strarr) - k):
            count = 0
            for string in strarr[index:(index + k + 1)]:
                count += len(string)
            lenghts_list.append(count)
        starting_index = lenghts_list.index(max(lenghts_list))
        "".join(str(strarr[starting_index:(k + 1)]))
    return longest_consecutive

