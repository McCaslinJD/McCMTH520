# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Jordan>
<MTH520>
<Date>

"""
import numpy as np

def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A = np.array([[4, -2, 4], [1, 5, -9]])
    B = np.array([[2, 6, -5, 3],[5, -8, 9, 7],[9, -3, -2, -2]])
    return A.dot(B)
    raise NotImplementedError("Problem 1 Incomplete")

print (prob1())

def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array([[3,1,4], [1, 5, 9],[-5,3,1]])
    C = A.dot(A)
    C = -C.dot(A) + 9* C - 15*A
    return C
    raise NotImplementedError("Problem 2 Incomplete")


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.

    """
    A = np.ones((7,7))
    B = -1 * np.tril(A) + 5* np.triu(A) -5* np.diag(np.diag(A))
    A = np.triu(A)
    C = A.dot(B.dot(A))
    return C.astype(np.int64)
    raise NotImplementedError("Problem 3 Incomplete")


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    mask = A <0
    A[mask] = 0
    return(A)
    raise NotImplementedError("Problem 4 Incomplete")

A = prob1();
print(prob4(A))

def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.arange(6).reshape(3,2)
    A = A.transpose()
    I = np.eye(3)
    C = -2* I
    B = np.tril(3* np.ones(3))
    R1 = np.hstack((np.zeros((3,3)),A.transpose(), I))
    R2 = np.hstack((A,np.zeros((2,5))))
    R3 = np.hstack((B, np.zeros((3,2)), C))
    M = np.vstack((R1,R2,R3))
    return M
    raise NotImplementedError("Problem 5 Incomplete")



def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    s = x.sum(axis =1)
    s = np.array([s]).transpose()
    M = np.tile(s, len(x[1,:]))
    M = np.divide(x,M)
    return M
    raise NotImplementedError("Problem 6 Incomplete")


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    return "Yeah, didn't do this one.... optional right?"
    raise NotImplementedError("Problem 7 Incomplete")
