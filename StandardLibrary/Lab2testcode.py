import calculator as cal
import time
import box
import sys
from random import randint
from itertools import combinations

def prob1(L):
    return [min(L),max(L), sum(L)/len(L) ]




def prob2():
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

def prob3(a,b):
    a = cal.product(a,a)
    b = cal.product(b,b)
    c = cal.sum(a,b)
    c = cal.sqrt(c)
    return c

def power_set(A):
    l = len(A)
    pset = []
    for n in range(l+1):
        new_sets = list(combinations(A,n))
        for s in new_sets:
            pset.append(s)
    return pset


def roll( s):
    if s <= 6:
        return randint(1,6)
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1+ d2

def shut_the_box():
    if len(sys.argv) == 3: 
        cheat = False;
        t = 0
        remaining = list(range(1,10))
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
                print("Oi!! What are you trying to pull you door nob? Bugger off, I don't want to play with a cheat")
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

def gametest():
    t = time.time()
    input('Stop timer by hitting enter')
    stop = time.time() 
    print(str(round(stop- t,2)))



shut_the_box()
    
 


