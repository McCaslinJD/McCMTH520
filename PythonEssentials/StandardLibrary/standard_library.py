# standard_library.py
import calculator as cal

"""Python Essentials: The Standard Library.
<Name>
<Class>
<Date>
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    
    return [min(L),max(L), sum(L)/len(L) ]
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    x = 1       #int
    y = x
    y = 2
    print("does x =y?", x == y)      # False, so Immutable

    mystr1 = "oops I did it" #str
    mystr2 = mystr1
    mystr2 ="oops I did it" + "again..."
    print(  "does mystr1 = mystr2?", mystr1 == mystr2) #False, so Immutable

    mylist1 = [1,2,3,4,5]   #lists
    mylist2 = mylist1
    mylist2[1] = 0
    print(  "does mylist1 = mylist2?", mylist1 == mylist2) #True, so Mutable

    myset1 = {"Bad Religion", "Anti-flag" , "Minor Threat", "Operation Ivy", "NOFX", "Dead Kennedeys", "Rancid"} #Sets
    myset2 = myset1
    myset2.add("Reel Big Fish")
    print(  "does myset1 = myset2?", myset1 == myset2) #True, so Mutable

    mytuple1 = (1,2,3,4)   #Tuples
    mytuple2 = mytuple1
    mytuple2 += (1,)

    print(  "does mytuple1 = mytuple2?", mytuple1 == mytuple2) #False, so Immutable

    return (x == y, mystr1 == mystr2, mylist1 == mylist2, myset1 == myset2, mytuple1 == mytuple2 )
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    a = cal.product(a,a)
    b = cal.product(b,b)
    c = cal.sum(a,b)
    c = cal.sqrt(c)
    return c
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    l = len(A)
    pset = []
    for n in range(l+1):
        new_sets = list(combinations(A,n))
        for s in new_sets:
            pset.append(s)
    return pset
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
