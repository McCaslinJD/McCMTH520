import numpy as np


def is_drazin(A,Ad,k):
    if A.dot(Ad) != Ad.dot(A):
        return False
    else:
        return True

B = np.array([[1, 1, 3],[5, 2, 6],[-2, 1, -3]])
Bd = np.zeros([3,3])

print (is_drazin(B,Bd,3))