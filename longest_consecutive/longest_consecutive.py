"""
You are given an array strarr of strings and an integer k. 
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""

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


print(generate_longest_consecutive_string(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 2), "oocccffuucccjjjkkkjyyyeehh")
