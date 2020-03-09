# ----------------------------------------------------------------------
# Name:        lecture12
# Purpose:     Demonstrate context managers
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing some definitions to be used in lecture 12.

A Timer context manager that keeps track of the elapsed time in seconds.
A Transaction context manager to manage transactions on accounts.
A version of the timer context manager implemented with the decorator.
A version of the transaction manager implemented with the decorator.

"""
import time
import copy
from lecture10 import Account
from contextlib import contextmanager


class Timer:

    """
    A timer context manager that keeps track of the elapsed time
    Arguments: None
    Attributes: start_time (float): time when the context is entered
    """

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f'Elapsed time = {end_time - self.start_time:.4f}s')


class Transaction:

    """
    Transaction context manager to manage transactions on accounts.
    A transaction is either entirely successful or rolled back (voided).
    Argument:
    account: Account object
    Attributes:
    account: Account object
    working: ?
    """

    def __init__(self, account):
        self.account = account

    def __enter__(self):
        self.working = copy.copy(self.account)
        return self.working

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
           self.account.balance = self.working.balance
           print('Transaction complete.')
        else:
            print(f'{exc_value}: void transaction.')
            return True

@contextmanager
def timer():
    """
    A timer context manager that keeps track of the elapsed time
    :yield: None
    """
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f'Elapsed time = {end_time - start_time:.4f}s')


@contextmanager
def transaction(account):
    """
    A transaction context manager to manage transactions on accounts.
    :param account: Account object
    :yield: Account working object
    """
    working = copy.copy(account)
    try:
        yield working
    except Exception as error:
        print(f'{error}: void transaction.')
    else:
        account.balance = working.balance
        print('Transaction complete.')


def main():
    # Use the various context managers
    with Timer():
        for i in range(10000):
            result = i ** 2


if __name__ == "__main__":
    main()
