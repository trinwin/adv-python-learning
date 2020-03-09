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
def top_midterm(grades):
    """
    Takes in a dictionary of student names and their corresponding
    grades & returns the name of the student with highest midterm score.
    If an empty dictionary is passed in then None is returned

    :param grades: dictionary of students and their grades
    :return: name of student with highest midterm
    """
    return None if not grades else max(grades,
        key = lambda name: grades[name][2])

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
                 curr+=1
                 count+=1
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


def learn(filename):
    """

    :param filename:
    :return:
    """
    map = dict()
    with open(filename, 'r', encoding='UTF-8') as file:
        data = file.read().replace('\n', ' ').lower()
        translator = str.maketrans('', '', string.punctuation)
        words = data.translate(translator).split()
        for idx, each_word in enumerate(words):
            next_word = words[idx+1] if idx < len(words)-1 else ""
            if not map.get(each_word, 0):
                map[each_word] = [next_word] if next_word else []
            elif map.get(each_word, 0):
                if next_word:
                    map.get(each_word).append(next_word)
    return map


# Include the statement below at the top of the babble definition



def babble(filename, num_words = 8):
    random.seed(100)
    dictionary = learn(filename)
    all_keys = list(dictionary)
    print(all_keys)
    key = random.choice(all_keys)
    sentence = key + " "
    while num_words-1:
        new_word = random.choice(dictionary[key])

        sentence += new_word + " "
        num_words -= 1
    return sentence


def main():
    # You may use the main function to test your function definitions.

    empty_class = {}
    # print(longest_sequence(4, 10, 8, 3, 2, 11, 9, 40, 7, 7, 8, 4, 12))
    # print(longest_sequence(100, 202, 5, 2))
    # print(longest_sequence())
    # print(longest_sequence(60))
    # print(greet('Spartans'))  # sapartansa hllo
    # print(repeat("Special cases aren't special enough to break the rules", 2))
    # print(repeat("Special cases aren't special enough to break the rules", 2))
    # print(greet('Spartans'))  # sapartansa hllo

    print(learn("spider.txt"))
    # print(learn("yesterday.txt"))

    print(babble("spider.txt", 5))




if __name__ == '__main__':
    main()
