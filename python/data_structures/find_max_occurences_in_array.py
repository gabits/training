# Find the element that occurs in the array the most
A = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4]

occurences = [(A[0], 1)]
for i in range(len(A[1:])):
    if A[i] == occurences[i - 1][0]:
        count = occurences[i - 1][1] + 1
    else:
        count = 1
    occurences.append(tuple(element, count))

n_with_max_occurences: int = occurences[0][0]
for i in range(len(occurences[1:])):
    if occurences[i][1] > n_with_max_occurences:
        n_with_max_occurences = occurences[i][0]
return n_with_max_occurences
