# ----------------------------------------------------------------------
# Name:        homework3
# Purpose:     Practice Manipulating Sequence Data Types
#
# Author(s):   Mandeep Pabla, Trinh Nguyen
# ----------------------------------------------------------------------
"""
Implement various functions to practice manipulating sequence data types

Q1: transpose
Q2: grader
Q3: has_duplicates
Q4: remove_vowels
Q5: same_word_count
"""


def transpose(m):
    """
    Return a list representing the transpose of that matrix using
    list comprehension
    :param m: list - a nested list representing a matrix
    :return: list - representing the transpose of m
    """
    return [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))]


def grader(grades, threshold=4):
    """
    Calculate the average of the grades given a list of grades and a
    threshold. If the number of grades in the list exceeds the threshold,
    lowest grade is dropped from the list and the average of the remaining
    grades is returned.
    :param grades: list - list of grades
    :param threshold: int - number of grade candidate need to have and
    its default value is 4
    :return: int - the average of the grades
    """
    if not grades:
        return 0
    if len(grades) > threshold:
        grades.remove(min(grades))
    return sum(grades) / threshold


def has_duplicates(s):
    """
    Takes in any sequence (string, list or tuple) and returns True if the
    sequence contains duplicates and False otherwise.
    :param s: any sequence (string, list or tuple)
    :return: boolean - True if the sequence contains duplicates and
    False
    otherwise
    """
    # return True if len([x for x in set(s) if s.count(x) > 1]) else False
    return len(s) != len(set(s))


def remove_vowels(s):
    """
    Takes in a string and returns another string with all the characters of
    the original string except the vowels
    :param s: string - any string
    :return: string - original string s except the vowels
    """
    return ''.join([c for c in s if c not in 'aeiouAEIOU'])


def same_word_count(s1, s2):
    """
    Takes in 2 strings and then returns True if the strings have the same
    number of words and False otherwise.
    :param s1: string - any strings of words
    :param s2: string - any string of words
    :return: boolean - True if the strings (s1, s2) have the same number of
    words
    and False otherwise
    """
    # return True if len(s1.split()) == len(s2.split()) else False
    return len(s1.split()) == len(s2.split())


def main():
    # You may use the main function to test your function definitions.
    pass


if __name__ == '__main__':
    main()
