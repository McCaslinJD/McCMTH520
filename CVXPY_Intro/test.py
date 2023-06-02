
import numpy as np
import cvxpy as cp


def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3,nonneg = True)
    c = np.array([2,1,3])
    objective = cp.Minimize( c.T @ x)
    G = np.array([[1, 2, 0],[0,1,-4],[-2,-10,-3]])
    P = np.eye(3)
    h = np.array([0.,1.,-12.]).transpose()
    constraints = [G @ x <= h, P @ x >= 0]
    problem = cp.Problem(objective,constraints)
    problem.solve()
    return (type(x.value)) 



    raise NotImplementedError("Problem 1 Incomplete")


def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    (n,m) = A.shape
    x = cp.Variable(m, nonneg = False)
    objective= cp.Minimize(cp.norm(x,1))
    constraints = [ A @ x == b]
    problem = cp.Problem(objective,constraints)
    problem.solve()
    return (x.value, problem.solve())


    raise NotImplementedError("Problem 2 Incomplete")

A = np.array([[1, 2, 1, 1],[0,3,-2,-1]])
b = np.array([7,4])



def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(6, nonneg = True)
    c = np.array([4,7,6,8,8,9])
    objective = cp.Minimize(c.T @ x)
    h = np.array([7,2,4]).transpose()
    b = np.array([5,8]).transpose()
    A = np.array([[1,0,1,0,1,0],[0,1,0,1,0,1]])
    G = np.array([[1,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,1]])
    P = np.eye(6)
    constraints = [ A @ x == b, G @ x <= h, P @ x >= 0]
    problem = cp.Problem(objective, constraints)
    problem.solve()

    return(x.value,  problem.solve() )
    raise NotImplementedError("Problem 3 Incomplete")


def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    Q = np.array([[3/2,1,.5],[1,2,1],[.5,1,3/2]])
    r = np.array([3,0,1])
    x = cp.Variable(3)
    prob = cp.Problem(cp.Minimize( cp.quad_form(x,Q) + r.T @ x)  )
    prob.solve()
    return (x.value, prob.solve())
    raise NotImplementedError("Problem 4 Incomplete")


def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    (m,n) = A.shape
    x = cp.Variable(n, nonneg = True)
    obective = cp.Minimize(cp.norm( (A @ x) - b ,2))
    r = np.ndarray((n))
    r = np.ones_like(r)
    constraint = [ r.T @ x == 1]
    problem = cp.Problem(obective, constraint)
    problem.solve()
    return (x.value, problem.solve())
    

    raise NotImplementedError("Problem 5 Incomplete")

print(prob5(A,b))

