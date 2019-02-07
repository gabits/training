"""
1. Fast exponentiation
For a**n, the result is always 1 if n = 0 and a if n = 1.
After this, the most basic form of exponentiation is when n = 2, because
we perform the basic multiplication of a x a.
Therefore, we can reduce the function with an even power to call itself until
it reaches the result b for the multiplication on base 2 (a x a), then build
repeatedly on this logic, performing b x b and on. With an odd number, we just
need to perform the previous operation with n - 1 (which would be an even power),
then multiply the result by a.
"""
def fast_exponentiation(a, n):
    if n == 0:
        exp = 1
    elif n == 1:
        exp = a
    elif n == 2:
        exp = a * a
    elif n % 2 != 0:
        exp = a * fast_exponentiation(a, (n - 1))
    elif n % 2 == 0:
        exp_by_half_of_the_power = fast_exponentiation(a, (n / 2))
        exp = exp_by_half_of_the_power * exp_by_half_of_the_power
    return exp


"""
2. Missing number problem with a sorted array
"""

def binary_search(A):
    while len(A) > 2:
        expected = A[0]
        half = len(A) // 2
        if A[half] == expected:
            # If the number in medium position is just as expected,
            # the missing number is later on the list
            A = A[half:]
        else:
            A = A[:(half + 1)]
    if A[1] - A[0] == 1:
        return "No missing numbers"
    else:
        return A[1]


"""
3. Subarray problem
3.1. Iterative algorithm
"""

def nested_loops(A, B):
    result = True
    for b in B:
        is_b_fulfilled = False
        for a in A:
            if b == a:
                is_b_fulfilled = True
        if not is_b_fulfilled:
            result = False
    return “YES” if result else “NO”


"""
3.2. Recursive algorithm
Based on the resolution with nested loops, it was possible to create a recursive function to
express what each one of the loops would check for.
"""

def is_b_in_A(b, A, start_at=1):
    result = False
    if len(A) == 0:
        result = False
    elif len(A) == 1 and A[0] != b:
        result = False
    elif A[0] == b:
        result = True
    else:
        result = is_b_in_A(b, A[1:], (start_at + 1))
    return result


def is_B_in_A(B, A, start_at=1):
    result = False
    if len(B) == 0 or len(B) > len(A):
        result = False
    elif is_b_in_A(B[0], A):
        if len(B) == 1:
        result = True
        else:
        result = is_B_in_A(B[1:], A)
    else:
        result = False
    return “YES” if result else “NO”


def test_is_B_in_A():
    assert is_B_in_A([2, 3, 4], [2, 3, 4]) == True
    assert is_B_in_A([2, 3, 4], [3, 4, 2]) == True
    assert is_B_in_A([2, 3, 4], [1, 5, 3, 4, 2, 9, 8, 4]) == True
    assert is_B_in_A([2, 3, 4], [3, 2, 12, 13, 15, 2, 5]) == False
    assert is_B_in_A([2, 4], [3, 2, 1, 5, 7, 18, 95, 10]) == False
    assert is_B_in_A([1, 3], [3, 2]) == False
    assert is_B_in_A([], [3, 2]) == False
    assert is_B_in_A([2, 3, 4], []) == False
    test_is_B_in_A()


"""
3.3 Arrays sorted
Based on the MergeSort algorithm, replicated in a simple manner with the following code:
"""

def merge_sorted_lists(array_1, array_2):
    merged_list = []
    if len(array_1) >= len(array_2):
        A = array_1
        B = array_2
    else:
        A = array_2
        B = array_1
    while len(A) > 0:
        if len(B) == 0:
            merged_list.append(A[0])
            A = A[1:]
        elif A[0] > B[0]:
            merged_list.append(B[0])
            B = B[1:]
        else:
            merged_list.append(A[0])
            A = A[1:]
    return merged_list


"""
It was possible to perform minor tweaks on it so the function would perform value
comparisons using flags and if statements. Although the size of the array is changed during
various iterations, because it is meant only to cut to minor elements, but not modify the
original array, the complexity is kept at O(n).
"""

def is_B_in_A_ordered(B, A):
    if len(B) > len(A) or len(B) == 0 or len(A) == 0:
        return False
    b_in_A = False
    while len(B) > 0:
        if A[0] == B[0]:
            b_in_A = True
            if len(B) == 1:
                break
            else:
                B = B[1:]
        else:
            A = A[1:]
            b_in_A = False
    return b_in_A


def test_is_B_in_A_ordered():
    assert is_B_in_A_ordered([1, 2, 3, 4], [1, 2, 3, 4, 5]) == True
    assert is_B_in_A_ordered([], [4, 5]) == False
    assert is_B_in_A_ordered([57, 59], [55, 56, 57, 58, 59]) == True
    assert is_B_in_A_ordered([2, 3, 4], []) == False
    test_is_B_in_A_ordered()
