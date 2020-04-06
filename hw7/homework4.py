# ----------------------------------------------------------------------
# Name:    homework4
# Purpose: Practice Dictionaries, Comprehensions & Generator Expressions
#
# Author(s): Mandeep Pabla & Trinh Nguyen
# ----------------------------------------------------------------------
"""
Implement various functions with dictionaries and generator expressions.

Q1: top_students
Q2: final_grade
Q3: boost_grade
Q4: word_lengths
Q5: geometric_sum
"""
import string


def top_students(grades, n=3):
    """
    The function returns a list that contains the names of the top n
    students with the highest grades.
    :param grades: a dictionary representing student grades
    :param n: int - number of students
    :return: list that contains the names of the top n students
    with the highest grades
    """
    return sorted(grades, key=grades.get, reverse=True)[:n]


def final_grade(grades, n=1):
    """
    The function returns a new dictionary that contains the names of
    the students and their updated grade after the extra credit points
    have been added. The function does not modify original dictionary.
    :param grades: dictionary - represent student grades
    :param n: int - extra credit
    :return: dictionary that contains the names of students and their
    updated grade after the extra credit points
    have been added.
    """
    return {s: grades[s] + n for s in grades}


def boost_grade(iclicker, exam):
    """
    The function returns a new dictionary that contains the names of
    the students and their grade after the iClicker points have been
    processed. The function does not modify the original dictionaries.
    :param iclicker: grades: dictionary - represent iclicker points
    :param exam: grades: dictionary - represent student midterm grades
    :return: dictionary that contains the names of the students and
    their grade after the iClicker points have been processed
    """
    if not iclicker and not exam:
        return {}
    if not iclicker:
        return exam

    iclicker_avg = sum(iclicker.values()) / len(iclicker)
    if not exam:
        return {student: 1 if iclicker[student] >= iclicker_avg else 0 for
                student in iclicker}

    students = set(iclicker).union(set(exam))
    return {s: 0 if not exam.get(s, 0) else
            (exam[s] + 1 if iclicker.get(s, -1) >= iclicker_avg else exam[s])
            for s in students}


def word_lengths(phrase):
    """
    The function returns a dictionary where keys are the words in the
    string (in lower case and with no punctuation) and the values are
    lengths of these words.
    :param phrase: string - contains many words, space and punctuations
    :return: dictionary where keys are the words in the string (in lower
    case and with no punctuation) and the values are
    lengths of these words.
    """
    return {} if not phrase else {word.strip(string.punctuation): len(
        word.strip(string.punctuation)) for word in phrase.lower().split()}


def geometric_sum(n):
    """
    The function takes as a parameter an integer n and returns the sum
    of 1/2 + 1/4 + 1/8 + ... + 1/n
    :param n: int - any number
    :return: returns the sum of 1/2 + 1/4 + 1/8 + ... + 1/n
    """
    if not n:
        return 0
    return sum(1 / (2 ** i) for i in range(1, n + 1))


def main():
    # You may use the main function to test your function definitions.
    pass

if __name__ == '__main__':
    main()
