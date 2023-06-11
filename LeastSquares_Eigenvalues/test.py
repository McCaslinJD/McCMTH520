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
    data = np.load("housing.npy")
    year = data[:,0]
    n = len(year)
    x = np.linspace(min(year),max(year), 100)
    price = data[:,1].reshape((n,1))
    plt.scatter(year,price, label = 'Data')
    A = np.vander(year,12)
    for i in range(1,5):
        n =  i * 3 
        lab = "Polynomial fit of degree " + str(n)
        An = A[:,12-n:12]
        l = least_squares(An,price)
        f = np.poly1d(l.transpose()[0])
        y = f(x)
        plt.plot(x,y, label = lab)
    plt.legend()
    plt.xlabel("Years since 2000")
    plt.ylabel('Housing Price Index')
    plt.title('Problem 3')
    return plt.show()


polynomial_fit()


