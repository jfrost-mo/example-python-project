def add_one(n):
    """
    Increments the input by one.
    
    Parameters
    ----------
    n: int or float
        The starting number which is added too.
    
    Returns
    -------
    int or float
        The result of adding one.
    
    Raises
    ------
    TypeError
        If n is not a number.
    
    Notes
    -----
    This is a simple function to demonstrate how they should be generally
    written. It impliments addition [1]_

    The operation of this function is described by the following equation:
    
    .. math:: n_{final} = n_{inital} + \\int^{1}_{0} \\frac{x}{1} dx

    References
    ----------
    .. [1] Wikipedia contributors, "Addition," Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Addition&oldid=1112352709 

    Examples
    --------
    >>> Example.example.add_one(3)
    4
    """
    return n + 1


def is_even(n):
    """
    Tests if the input is even.
    
    Parameters
    ----------
    n: int or float
        The number being tested.
    
    Returns
    -------
    bool
        True for even, False for odd.
    
    Raises
    ------
    TypeError
        If n is not a number.
    
    Examples
    --------
    >>> Example.example.is_even(2)
    True

    >>> Example.example.is_even(3)
    False
    """
    if n % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # Given this is a libary this bit shouldn't really exist.
    print("This is an example program.")

