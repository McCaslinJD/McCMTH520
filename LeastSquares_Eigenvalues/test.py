import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt

def least_squares(A,b):
    At = A.transpose()
    N = At.dot(A)
    Q, R = la.qr(A, mode = 'economic')
    B = Q.transpose().dot(b)
    x = la.solve_triangular(R,B)
    return x


def prob2():
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
    plt.scatter(year,price)
    plt.plot(x,y)
    plt.show()


def polynomial_fit():
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


