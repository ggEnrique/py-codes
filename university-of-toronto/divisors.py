def get_divisors(num, possible_divisors):
    """
    (int, list of int) -> list of int

    Return a list of divisors of num that are present in the possible_divisors list.
    Zeroes in the possible_divisors list are ignored.

    :param num: The integer for which divisors are to be found.
    :param possible_divisors: A list of integers containing potential divisors of num.
    :return: A list of integers containing the divisors of num found in possible_divisors.

    >>> get_divisors(12, [1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 6]
    >>> get_divisors(15, [0, 5, 3, 4, 0])
    [5, 3]
    >>> get_divisors(0, [1, 2, 3])
    []
    """

    divisors = []
    for item in possible_divisors:
        if item != 0 and num != 0 and num % item == 0:
            divisors.append(item)
    return divisors


import doctest

doctest.testmod()
