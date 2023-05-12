import numpy as np
from matplotlib import pyplot as plt

def var_of_means(n):
    A = np.random.normal(size = (n,n))
    m = np.mean(A, axis = 1)
    return float(np.var(m))

def prob1():
    x = np.arange(1,11) * 100
    y  = np.array([var_of_means(100)])
    for i in np.arange(2,11):
        n = i * 100
        n = var_of_means(n)
        y = z = np.append(y,np.array([n]))
    plt.plot(x,y)
    plt.show()


def prob2():
    x = np.linspace(-np.pi, np.pi, 100)
    ys = np.sin(x)
    yc = np.cos(x)
    yat = np.arctan(x)
    plt.plot(x,ys, label = "Sine")
    plt.plot(x,yc, label = "Cosine")
    plt.plot(x,yat, label = "ArcTangent")
    plt.legend()

    return plt.show()

def prob3():
    x = np.linspace(-2,6,200)
    mask1 = x > 1
    mask2 = x < 1
    x1 = x[mask1]
    x2 = x[mask2]
    y1 = 1/(-1 + x1)
    y2 = 1/(-1+ x2)
    plt.plot(x1,y1,'m--', lw = 4)
    plt.plot(x2,y2, 'm--', lw = 4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    return plt.show()

def prob4():
    x = np.linspace(0, 2*np.pi, 200)
    y1 = np.sin(x)
    y2 = 2* np.sin(x)
    y3 =  np.sin(2* x)
    y4 = 2*np.sin(2 * x)
    ax1 = plt.subplot(2,2,1)
    ax2 = plt.subplot(2,2,2,)
    ax3 = plt.subplot(2,2,3)
    ax4 = plt.subplot(2,2,4)
    ax1.plot(x,y1, 'g')
    ax1.set_title('Sin(x)')
    ax2.plot(x,y2, 'b--')
    ax2.set_title('2Sin(x)')
    ax3.plot(x,y3, 'r--')
    ax3.set_title('Sin(2 x)')
    ax4.plot(x,y4, 'b:')
    ax4.set_title('2 Sin(2x)')
    plt.suptitle("Problem 4")
    plt.axis([0,2* np.pi, -2, 2])
    return plt.show()


def prob5():
    x = np.linspace(-2 * np.pi, 2 * np.pi)
    y = x
    X, Y = np.meshgrid(x,y)
    Z = np.sin(X) * np.sin(Y) / (X * Y)
    plt.subplot(1,2,1)
    plt.contour(X,Y,Z, 20, cmap = 'coolwarm' )
    plt.colorbar()

    plt.subplot(1,2,2)
    plt.pcolormesh(X,Y,Z, cmap = 'coolwarm', shading = 'auto')
    plt.colorbar()

    plt.axis([-2* np.pi, 2* np.pi,-2* np.pi, 2* np.pi])
    return plt.show()

prob5()