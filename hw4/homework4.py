# ----------------------------------------------------------------------
# Name:    homework4
# Purpose: Practice Dictionaries, Comprehensions & Generator Expressions
#
# Author(s):
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

# Enter your 5 function definitions here

def main():
    # You may use the main function to test your function definitions.
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

def top_students(student_grades, n=3):
    return sorted(student_grades, key=student_grades.get, reverse=True)[:n]

def final_grade(student_grades, n=1):
    return {student: student_grades[student] + n for student in student_grades}

if __name__ == '__main__':
    main()
