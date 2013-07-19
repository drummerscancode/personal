import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    >>> num_buses(2)
    1
    >>> num_buses(49)
    1
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    >>> num_buses(99)
    2
    >>> num_buses(100)
    2
    >>> num_buses(101)
    3
    """
    return int(math.ceil(n / 50.0))
	

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    ### insert smallest interesting case, mixed 2 and 2
    ### smallest interesting case, order (not really required)
    ### numbers of int, float, long, complex? not really required
    
    >>> stock_price_summary([]) # size: empty list 
    (0, 0)
    >>> stock_price_summary([0]) # size: one element, dichotomy 
    (0, 0)
    >>> stock_price_summary([1]) # size: one element, dichotomy 
    (1, 0)
    >>> stock_price_summary([-1]) # size: one element, dichotomy
    (0, -1)
    >>> stock_price_summary([0.01, 0.03, 0.02]) # size smallest interesting case, dichotomy only gains
    (0.06, 0)
    >>> stock_price_summary([-0.02, -0.14]) # size smallest interesting case, dichotomy only losses
    (0, -0.16)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    losses = 0
    gains = 0
    for item in price_changes:
        if item < 0:
            losses += item
        elif item > 0:
            gains += item
    return (gains, losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 1)
    >>> nums
    [6, 2, 3, 4, 5, 1]
    """
    for i in range(k):
        L[i], L[len(L) - k + i] = L[len(L) - k + i], L[i] 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
