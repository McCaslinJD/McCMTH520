# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Jordan McCaslin>
<MTH520>
<5/8/2023>
"""
import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    At = A.transpose()
    Q, R = la.qr(A, mode = 'economic')
    B = Q.transpose().dot(b)
    x = la.solve_triangular(R,B)
    return x
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load("housing.npy")
    year = data[:,0]
    n = len(year)
    price = data[:,1].reshape((n,1))
    year = year.reshape((n,1))
    constant = np.ones([n,1])
    A = np.hstack((year,constant))
    l = least_squares(A,price)
    x = np.linspace(min(year),max(year), 100)
    y = l[0]*x + l[1]
    plt.scatter(year,price, label = 'Data Points')
    plt.plot(x,y, label = " Least Squares Fit")
    plt.legend()
    plt.xlabel("Years Since 2000")
    plt.ylabel("Housing Price Index")
    return plt.show()
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load("LeastSquares_Eigenvalues\housing.npy")
    year = data[:,0]
    n = len(year)
    x = np.linspace(min(year),max(year), 100)
    price = data[:,1].reshape((n,1))
    plt.scatter(year,price, label = 'Data')
    A = np.vander(year,12)
    lab = "Polynomial fit of degree " + str(3)
    An = A[:,12-4:12]
    l = least_squares(An,price)
    f = np.poly1d(l.transpose()[0])
    y = f(x)

    ax1 = plt.subplot(2,2,1)
    ax2 = plt.subplot(2,2,2)
    ax3 = plt.subplot(2,2,3)
    ax4 = plt.subplot(2,2,4)
    ax1.plot(x,y, label = lab)
    ax1.scatter(year,price,label = 'Data')
    ax1.set_title('Degree 3 fit')

    lab = "Polynomial fit of degree " + str(6)
    An = A[:,12-7:12]
    l = least_squares(An,price)
    f = np.poly1d(l.transpose()[0])
    y = f(x)
    ax2.plot(x,y, label = lab)
    ax2.scatter(year,price,label = 'Data')
    ax2.set_title('Degree 6 fit')

    lab = "Polynomial fit of degree " + str(9)
    An = A[:,12-10:12]
    l = least_squares(An,price)
    f = np.poly1d(l.transpose()[0])
    y = f(x)
    ax3.plot(x,y, label = lab)
    ax3.scatter(year,price,label = 'Data')
    ax3.set_title('Degree 9 fit')

    lab = "Polynomial fit of degree " + str(12)
    An = A
    l = least_squares(An,price)
    f = np.poly1d(l.transpose()[0])
    y = f(x)
    ax4.plot(x,y, label = lab)
    ax4.scatter(year,price,label = 'Data')
    ax4.set_title('Degree 12 fit')



    
    plt.xlabel("Years since 2000")
    plt.ylabel('Housing Price Index')
    plt.suptitle('Problem 3')
    return plt.show()

polynomial_fit()

def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
