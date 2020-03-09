# ----------------------------------------------------------------------
# Name:     generators
# Purpose:  Practice with Python generators
#
# Author:   Rula Khayrallah
# ----------------------------------------------------------------------
"""
Practice writing and using generator functions

A doubling sequence generator.
An infinite doubling sequence generator.
A hailstone sequence generator.
"""

def double_generator(limit):
    """
    Generate a sequence of powers of 2 starting at 1 and up to and
    including the limit specified.
    :param limit: (integer) upper limit of the sequence generated
    :yield: (integer) a power of two
    """
    current = 1
    while current <= limit:
        yield current
        current = current * 2

def infinite_double_generator():
    """
    Generate an infinite sequence of of powers of 2
    :yield:  (integer) a power of two
    """
    current = 1
    while True:
        yield current
        current = current * 2

def hailstone(number):
    # Remove the pass statement and type in your code below
    current = number
    while current > 1:
        yield current
        if current % 2 == 0:  # if current is even
            current = current // 2
        else:  # if current is odd
            current = 3 * current + 1
    yield current