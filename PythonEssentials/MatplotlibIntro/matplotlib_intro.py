# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Jordan McCaslin>
<MTH520>
<5-3-2023>
"""
import numpy as np
from matplotlib import pyplot as plt


# Problem 1
def var_of_means(n):
    A = np.random.normal(size = (n,n))
    m = np.mean(A, axis = 1)
    return np.var(m)
    raise NotImplementedError("Problem 1 Incomplete")

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    x = np.arange(1,11) * 100
    y  = np.array([var_of_means(100)])
    for i in np.arange(2,11):
        n = i * 100
        n = var_of_means(n)
        y = z = np.append(y,np.array([n]))
    plt.plot(x,y)
    
    return plt.show()

    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-np.pi, np.pi, 100)
    ys = np.sin(x)
    yc = np.cos(x)
    yat = np.arctan(x)
    plt.plot(x,ys, label = "Sine")
    plt.plot(x,yc, label = "Cosine")
    plt.plot(x,yat, label = "ArcTangent")
    plt.legend()

    return plt.show()
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
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
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
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


    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
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

    raise NotImplementedError("Problem 6 Incomplete")

prob1()
prob2()
prob3()
prob4()
prob6()