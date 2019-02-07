"""
3 Subarray problem
Consider the following task given two arrays A and B without repetitions (that
is, no double occurrences of the same element). Tha task is to check whether
each element of B is also an element of A without regard of the order.
For instance if A = [1, 2, 3, 4] and B = [2, 3, 1] then the answer is YES. If
however B = [1, 2, 5] then the answer is NO because 5 is not in A. Such a
problem is easy to solve using the set operations in Python. For this exercise
please do not use these operations. Marks will not be awarded for
solutions using the Python operations with sets
"""


"""
3.1 Iterative algorithm (20 points)
Design an O(n2) algorithm for the subarray problem.
Hint: use two nested loops. You need to think what to explore in the inner
and in the outer loops.
"""
A = [1, 2, 3, 4]
B = [2, 3, 1]
C = [2, 3, 5]


def iterative_check(a: list, b: list) -> str:
    b_in_a = True

    for b_element in b:
        b_element_in_a = False
        for a_element in a:

            if b_element == a_element:
                b_element_in_a = True
                break

        if not b_element_in_a:
            b_in_a = False
            break

    return 'YES' if b_in_a else 'NO'


assert iterative_check(A, B) == 'YES'
assert iterative_check(A, C) == 'NO'


"""
3.2 Recursive algorithm (20 points)
Design a recursive algorithm (no use of loops) for the subarray problem.
"""

A = [1, 2, 3, 4]
B = [2, 3, 1]
C = [2, 3, 5]


def recursive_check(a: list, b: list) -> str:
    pass


assert recursive_check(A, B) == 'YES'
assert recursive_check(A, C) == 'NO'



"""
3.3 Arrays sorted (20 points)
Assume that both A and B are sorted arrays and design an O(n) algorithm
under this assumption.
Hint: A possible solution is a simple modification of the Merge procedure
of MergeSort algorithm.
"""
A = [1, 2, 3, 4]
B = [2, 3, 1]
C = [2, 3, 5]


def sorted_check(a: list, b: list) -> str:
    pass


assert recursive_check(A, B) == 'YES'
assert recursive_check(A, C) == 'NO'
