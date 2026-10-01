#!/usr/bin/python3
"""Module for the minOperations function."""


def minOperations(n):
    """Return the fewest operations (Copy All, Paste) to get n 'H'.

    The answer is the sum of the prime factors of n.
    Returns 0 if n is not an integer greater than 1.
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
