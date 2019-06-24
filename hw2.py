import functools

"""
function that filter list with given function
"""
def myFilter(L, func):
    """
    :param L: list to filter
    :param func: function to filter with
    :return: filtered list
    """
    return [x for x in L if func(x)]


"""
function that returns true if number is quadric, false elsewhere
"""


def myQuadric(x):
    """
    :param x: Number
    :return: boolean value if x is quadric
    """
    sum = 0
    i = 1
    while sum < x:
        sum += i
        i += 2
        if sum == x:
            return True
    return False


"""
function that returns true if x is dividing in 3 
"""


def isDiv3(x):
    """
    :param x: number
    :return: true if number is dividing in 3, false elsewhere
    """
    return x % 3 == 0


"""
function that filters given list with multiple functions packed in list 
"""


def myFilterMulti(L, funcL):
    """
    :param L: list of values
    :param funcL: list of filter functions
    :return: filtered list that it's elements fulfill all the functions (AND)
    """
    boolist = []
    newList = []
    for l in L:
        for f in funcL:
            boolist.append(f(l))
        if functools.reduce(lambda a, b: a and b, boolist):
            newList.append(l)
        boolist = []
    return newList


"""
function that sums up the gimetric value of given string
"""


def gimetric_value(string):
    """
    :param string: string to calculate it's gematria
    :return: the gematria of the given string
    """
    sum = 0
    for l in string:
        num = 0
        if 65 <= ord(l) <= 90:
            num = ord(l) - 64
        elif 97 <= ord(l) <= 122:
            num = ord(l) - 96
        sum += num
    return sum
