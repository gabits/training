"""You are given a list/array which contains only integers (positive and negative). Your job is to sum only the numbers
that are the same and consecutive. The result should be one list.

Extra credit if you solve it in one line. You can assume there is never an empty list/array and there will always be an
integer.


Notes:
    - 1 == 1
    - 1 != -1


Examples:

        [1,4,4,4,0,4,3,3,1]
    Should return:
        [1,12,0,4,6,1]

         [1,1,7,7,3]
    Should return:
        [2,14,3]

        [-5,-5,7,7,12,0]
    Should return:
        [-10,14,12,0]

"""


def sum_consecutive_integers(o_list):
    new_list = [o_list[0]]
    for i in range(1, len(o_list)):
        if o_list[i] == o_list[i - 1]:
            new_list[len(new_list) - 1] += o_list[i]
        else:
            new_list.append(o_list[i])
    return new_list
