# python_intro.py
"""Python Essentials: Introduction to Python.
<Jordan McCaslin>
<MTH520>
<4/10/2023>
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")

# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    return 4/3 * 3.14159 * r**3
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print( a, "     ", b,"     ", c, d,e)
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.
    

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    l = len(s)
    l = l//2
    return s[:l]
    raise NotImplementedError("Problem 4 Incomplete")

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    l = len(s)
    return s[l:0:-1]+s[0]
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    my_list = [ 'bear', 'ant','cat', 'dog']
    my_list.append('eagle')
    my_list[2] = 'fox'
    my_list.pop(1)
    my_list = sorted(my_list,reverse = True)
    n = my_list.index('eagle')
    my_list[n] = 'hawk'
    l = len(my_list)
    my_list[l-1] = my_list[l-1]+ 'hunter'
    return my_list
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    vowels = { 'a', 'e', 'i', 'o', 'u'}
    if word[0] in vowels:
        word = word+'hay'
    else:
        word = word+word[0] + 'ay'
        word = word[1:]
    return word
    raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    n = range(100,1000,1)
    z=1
    for i in n:
        for j in n:
            x = str(i*j)
            y = x[::-1]
            if x == y:
                z = x
                factor1 = str(i)
                factor2 = str(j)
    print(factor1 + "times" + factor2 + "=" + z)
    raise NotImplementedError("Problem 7 Incomplete")

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    raise NotImplementedError("Problem 8 Incomplete")
