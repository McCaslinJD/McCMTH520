# standard_library.py
import calculator as cal
import time
import box
import sys
from random import randint
from itertools import combinations


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


def roll(s):
    if s <= 6:
        return randint(1,6)
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1+ d2



# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    remaining = list(range(1,10))
    if len(sys.argv) == 3: 
        cheat = False;
        t = 0
        
        tlimit = float(sys.argv[2])
        while t <= tlimit:                       #Initiate game
            print("Numbers left:" + str(remaining))         #List of numbers left
            print( 'Seconds left: ' + str(round(tlimit - t,2)))               #Time remaining
            r = roll(sum(remaining))
            box.isvalid(r, remaining)
            if box.isvalid(r, remaining) == False:
                print("You had" + str(remaining) + "left, but you rolled " + str(r)+ ". Yer luck's run out mate. You lose. " )
                break
            print('Roll:'+ str(r))
            start = time.time()                      #Start the round's timer
            choice = input("Which ones you removing mate?")
            choice = box.parse_input(choice, remaining)
            end = time.time()                        #End the round's timer

            t += end-start                           #total time used
            if sum(choice) != r:
                cheat = True

            for i in choice:                         #Checking that choice was with the rules
                if i in remaining == False:
                    cheat = True
                    
            if cheat == True:
                print("Oi!! What are you trying to pull you doorknob? Bugger off, I'm not playing with a cheat")
                break 

            for i in choice:                        #Removing the choosen numbers
                remaining.remove(i)

            if sum(remaining) == 0:                 #Win conditions
                print('Well played lad, you win!')
                break  
        if t > tlimit:
            print("Yer time's up lad, You lose.")
    

    else:                                           #Not enough arguments given
        print("Oi you doorknob, you never told me your name or how long we are playing. ")

    return sum(remaining)
    raise NotImplementedError("Problem 5 Incomplete")

shut_the_box(sys.argv[1], sys.argv[2])