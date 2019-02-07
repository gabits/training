"""
1 Missing number problem for arrays with a fixed length

Recall the missing number problem we considered in the class (also available on
the slides of lecture 1). In particular, we considered two algorithms, one with
nested loops and one without them. This question is about the first algorithm
(with nested loops). Assume that n = 10, the array is [1, 2, 3, 4, 5, 6, 7, 9, 10]
(number 8 is missing).


1. 10 points. How many iterations of the outer loop will be needed for the
program to learn that 8 is missing?
8 iterations


2. 10 points. How many iterations of the inner loop will be needed to find
out that 6 is in the array?
6! = 6 + 5 + 4 + 3 + 2 + 1 = 21 iterations in total,
6 iterations when j = 5 and i = 6

"""


"""
2 Missing number problem for arrays with an arbitrary length
For the same algorithm as in Question 1, assume that n is arbitrary and the
array is {1, 2, . . . , n − 1}, i.e. number n is missing.

i = 2,
for(i=1; i<=n; i++) //explore the numbers
    { int flag=0;
    for(j=0; j<n-1; j++) //explore the array indices
    {
    if(A[j]==i) //number found
    { flag=1;
    break;
    }}
    if(flag==0) return i; //return the number that has not been found
}

1. 7 points. How many iterations of the outer loop will be needed to discover
that number n is missing?

n iterations. Given that the algorithm
will run through all iterations that satisfy the loop condition.
Given that the outer loop iterates from 1 to n inclusive
(i=1; i<=n), the last iteration is number n.

2. 8 points. For each number i from 1 to n, how many iterations of the
inner loop will be needed to process that number?
i!, because it always satisfies the if condition and reaches the break clause
on iteration number i.

3. 5 points. Calculate the total number of loop iterations of the inner loop.
n!, given that this is the maximum number of iterations we reach with this
algorithm when n is not in the array.
"""



"""
3 Binary increment operation (20 points)
Consider a one-dimensional array A of 100 elements. That is, the elements are
A[0], . . . , A[99]. Suppose that the content of each element is either 0 or 1. That
is, you can treat the array as a binary number with A[0] being the leftmost digit.

1 Write a program PlusOne(A) that adds 1 to the number stored in the array. For
example, (assuming that the array contains only 3 elements) if A[0] = 0, A[1] =
1, A[2] = 1 then PlusOne modifies the array to A[0] = 1, A[1] = 0, A[2] = 0.
Remark. If the array A contains all ones then the result of increment should
be all zeroes.
"""

def PlusOne(A):
    n = len(A)
    for i in range(1, n + 1):
        if A[-i] == 0:
            A[-i] = 1
            break
        else:
            A[-i] = 0
    return A


def test_plus_one():
    assert PlusOne([0, 0, 1]) == [0, 1, 0]
    assert PlusOne([0, 1, 0]) == [0, 1, 1]
    assert PlusOne([1, 1, 1]) == [0, 0, 0]


test_plus_one()


"""
4 Processing a binary matrix (20 points)
Let A be a n×n two-dimensional array (matrix), the content of each element is
either 0 or 1. Write an O(n2) program that tests whether there are two 1 lying
on the same row or the same column in A.
Hint: Make sure that you use a single loop per row and column.
"""
def process_binary_matrix(A):
    # Returns a boolean whether is there a 1 on the same row or column
    n = len(A)
    is_1_repeated = False
    for i in range(n):
        # j == number of col or row
        is_1_in_row = False
        is_1_in_col = False
        for j in range(n):
            # Numbers in row are the same
            if (A[j][i] == 1 and is_1_in_row) or (A[i][j] and is_1_in_col):
                is_1_repeated = True
                break
            elif A[j][i] == 1 and A[i][j] == 1:
                is_1_in_row = True
                is_1_in_col = True
            elif A[j][i] == 1:
                is_1_in_row = True
            elif A[i][j] == 1:
                is_1_in_col = True
    return is_1_repeated


def test_process_binary_matrix():
    assert process_binary_matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]]) == False
    assert process_binary_matrix([[0, 0, 1], [0, 1, 1], [1, 0, 0]]) == True
    assert process_binary_matrix([[0, 1, 0], [0, 0, 0], [0, 1, 0]]) == True


test_process_binary_matrix()

"""
5 A constant time algorithm
1. 15 points. Assume that all the elements in the given array are pairwise
distinct. Design an O(1) algorithm that returns an element that is NOT
the smallest one in the array.


2. 5 points. Why would not your approach work for the case of repeated
elements in the array?
It would not work because in this case A[0] could be equal to A[1].
"""
def return_not_smallest(A):
    if A[0] > A[1]:
        return A[0]
    else:
        return A[1]
