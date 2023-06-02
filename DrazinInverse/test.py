import numpy as np
from scipy import linalg as la
from numpy.linalg import inv
from numpy.linalg import matrix_power


def is_drazin(A,Ad,k):
    if np.allclose(A.dot(Ad), Ad.dot(A)) == False:
        return False
    elif np.allclose(matrix_power(A,k+1).dot(Ad), matrix_power(A,k)) == False:
        return False
    elif np.allclose(Ad.dot(A).dot(Ad), Ad) == False:
        return False
    else:
        return True

def drazin_inverse(A, tol=1e-4):
    (n,n) = A.shape
    f1 = lambda x: abs(x) > tol
    f2 = lambda x: abs(x) < tol

    T1,Q1,k1 = la.schur(A, sort = f1)
    T2,Q2,k2 = la.schur(A, sort = f2)
    U = np.hstack((Q1[:,0:k1], Q2[:,0:n-k1]))
    invU = inv(U)
    V = invU.dot(A).dot(U)
    Z = np.zeros((n,n))
    if k1 != 0:
        invM = inv(V[:k1, :k1])
        Z[:k1,:k1] = invM

    return (U.dot(Z).dot(invU))



def laplacian(A):
    L = np.diag(np.sum(A, axis = 1)) - A
    return L
  

A = np.array([[0,1,0,0,1,1],[1,0,1,0,1,0],[0,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[1,0,0,1,0,0]])


def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    L = laplacian(A)
    (n,n,) = A.shape
    I = np.eye(n)
    R = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i!= j:
                tL = L.copy()
                tL[j,:] = I[j,:]
                tL = drazin_inverse(tL)
                R[i,j] = tL[i,i]

    return R

    raise NotImplementedError("Problem 3 Incomplete")
A = np.array([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])
#A = np.ones((3,3)) - np.eye(3)
#A = np.array([[1,3,0,0],[0,1,3,0],[0,0,1,3],[0,0,0,0]])
B = np.array([[1,3,0,0],[0,1,3,0],[0,0,1,3],[0,0,0,0]])
print(drazin_inverse(B))