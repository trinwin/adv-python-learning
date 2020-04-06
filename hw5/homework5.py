# ----------------------------------------------------------------------
# Name:    homework5
# Purpose: Practice working with Python functions and files
#
# Author(s):
# ----------------------------------------------------------------------
"""
Implement various functions

Q1: top_midterm
Q2: longest_sequence
Q3: encrypt decorator
Q4: learn
Q5: babble
"""
import string
import random

# Enter your 5 function definitions here

# Include the statement below at the top of the babble definition
# random.seed(100)

def main():
    # You may use the main function to test your function definitions.
    cs122 = {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
             'Dan': [90, 60, 70], 'Anna': [60, 80, 100],
             'Ryan': [100, 95, 80], 'Bella': [79, 70, 99]}
    empty_class = {}
    # print(top_midterm(cs122))
    # print(top_midterm(empty_class))
    # print(longest_sequence(4, 10, 8, 3, 2, 11, 9, 40, 7, 7, 8, 4, 12))
    # print(repeat("Special cases aren't special enough to break the rules", 2))
    print(greet('Spartans'))  # sapartansa hllo


def top_midterm(grades):
    return None if not grades else max(grades, key = lambda name: grades[name][2])

def longest_sequence(*args):
     if not args:
        return 0

     nums = set(args)
     num_of_counts = []
     for i in nums:
         if i-1 not in nums:
             curr = i
             count = 0
             while curr in nums:
                 curr+=1
                 count+=1
             num_of_counts.append(count)

     return max(num_of_counts)

def encrypt(function):
    def wrapper(*args):
        result = function(*args)
        result = result.lower()
        result = result.replace("e","")
        result = result.replace("s", "sa")
        result = result.split()
        result.reverse()
        return ' '.join(result)
    return wrapper

@encrypt
def greet(name):
    """
    Return a personalized hello message.
    :param name: (string)
    :return: (string)
    """
    return f'Hello {name}'

@encrypt
def repeat(phrase, n):
    """
    Repeat the specified string n times
    with a space character in between.
    :param phrase: (string)
    :param n: number of times the phrase will be repeated
    :return:
    """
    words = phrase.split()
    return ' '.join(n * words)

if __name__ == '__main__':
    main()
