import doctest

def square(x):
    """
    >>> square(2)
    4
    """
    
    return x * x

doctest.testmod()