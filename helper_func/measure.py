# ----------------------------------------------------------------------
# Name:     measure
# Purpose:  Measure and compare performance of different implementations
#
# Author:  Rula Khayrallah
# ----------------------------------------------------------------------
"""
Measure and compare performance of different implementations.

1.  Compare the performance of tuples vs lists.
2.  Compare the performance of adding the numeric elements of a sequence
    by iterating over the sequence vs using the built-in function sum.
"""
import timeit

def create_list():
    """
    Create a list of 10 integers.
    :return: None
    """
    new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def create_tuple():
    """
    Create a tuple of 10 integers.
    :return: None
    """
    new_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def add_loop(seq):
    """
    Add the elements of a numeric sequence.
    :param seq: range, list or tuple of numbers
    :return:  number -  the sum of the elements
    """
    total = 0
    for each_element in seq:
        total += each_element
    return total

def add_builtin(seq):
    """
    Add the elements of a numeric sequence.
    :param seq: range, list or tuple of numbers
    :return:  number -  the sum of the elements
    """
    total = sum(seq)
    return total

def main():
    print(f"""Creating a list:  {timeit.timeit("create_list()",
                                               globals=globals()):.4f}s""")
    print(f"""Creating a tuple: {timeit.timeit("create_tuple()",
                                               globals=globals()):.4f}s""")
    # Uncomment the statements below to run the second test
    print(f"""Adding with a loop: {timeit.timeit("add_loop(s)",
                                               setup = "s = range(100)",
                                               globals=globals()):.4f}s""")
    print(f"""Adding with sum:    {timeit.timeit("add_builtin(s)",
                                                setup = "s = range(100)",
                                                globals=globals()):.4f}s""")


if __name__ == "__main__":
    main()
