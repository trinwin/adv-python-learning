# ----------------------------------------------------------------------
# Name:    homework5
# Purpose: Practice working with Python functions and files
#
# Author(s): Mandeep Pabla and Trinh Nguyen
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


def top_midterm(grades):
    """
    Takes in a dictionary of student names and their corresponding
    grades & returns the name of the student with highest midterm score.
    If an empty dictionary is passed in then None is returned
    :param grades: dictionary of students and their grades
    :return: name of student with highest midterm
    """
    return None if not grades else max(grades,
                                       key=lambda name: grades[name][2])


def longest_sequence(*args):
    """
    Takes in a number of integers and counts the longest
    consecutive sequence of integers efficiently. If no number
    of arguments is passed in then 0 is returned.
    :param args: arbitrary number of integers arguments
    :return: length of longest consecutive sequence of integers
    """
    if not args:
        return 0

    nums = set(args)
    num_of_counts = []
    for i in nums:
        if i-1 not in nums:
            curr = i
            count = 0
            while curr in nums:
                curr += 1
                count += 1
            num_of_counts.append(count)

    return max(num_of_counts)


def encrypt(function):
    """
    This decorator will encrypt strings by removing all occurrences of
    the letter e, adding an 'a' after each occurrence of the letter s
    and reversing the order of the words. It will return a lowercase
    version of the string.
    :param function: function that returns a string
    :return: wrapper that encrypts the string
    """

    def wrapper(*args):
        result = function(*args)
        result = result.lower()
        result = result.replace("e", "")
        result = result.replace("s", "sa")
        result = result.split()
        result.reverse()
        return ' '.join(result)
    return wrapper


@encrypt
def greet(name):
    """
    Return a personalized hello message.
    :param name: (string) - name
    :return: (string) - a personalized hello message.
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


def learn(filename):
    """
    Opens the file specified, reads it  and learns the words used in
    it as well as some basic structure information as so how the words
    are ordered in a sentence.
    :param filename: string - name of file
    :return: dict - each word is mapped to a list of all the words
    that immediately follow it in the input file
    """
    my_dict = dict()
    with open(filename, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for i, each_line in enumerate(lines):
            if each_line.strip():
                prev_word = ""
                for j, word in enumerate(each_line.lower().split()):
                    word = word.strip(string.punctuation)
                    if word:
                        if my_dict and not prev_word:
                            counter = 1
                            while lines[i-counter] in ['\n', '\r\n']:
                                counter += 1
                            prev_word = lines[i-counter].split()[-1]\
                                .lower().strip(string.punctuation)
                        if not my_dict.get(word, 0):
                            my_dict[word] = []
                        if prev_word:
                            my_dict.get(prev_word).append(word)
                        prev_word = word
    return my_dict


def babble(filename, num_words=8):
    """
    An infinite random sentence generator function that will  generate
    nonsensical sentences of a given length, loosely modeled after a
    specified text file.
    :param filename: string - name of file
    :param num_words: int - maximum number of words in sentence
    :return: string made up sentence based on dictionary of input file
    """
    random.seed(100)
    dictionary = learn(filename)
    all_keys = list(dictionary)

    while True:
        lst = []
        counter = num_words
        key = random.choice(all_keys)
        lst.append(key)
        counter -= 1
        while counter:
            while not dictionary[key]:
                key = random.choice(all_keys)
                lst.append(key)
                counter -= 1
            if counter:
                new_word = random.choice(dictionary[key])
                lst.append(new_word)
                counter -= 1
            key = new_word
        yield ' '.join(lst)


def main():
    # You may use the main function to test your function definitions.
    pass


if __name__ == '__main__':
    main()
