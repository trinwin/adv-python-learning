# ----------------------------------------------------------------------
# Name:    homework7
# Purpose: Write 5 test cases for the 5 functions in hw4
#
# Author(s): Mandeep Pabla and Trinh Nguyen
# ----------------------------------------------------------------------

import unittest
import homework4 as hw4


class TestQ1(unittest.TestCase):
    """
    Test case for the normal execution of the top_student function
    """

    def setUp(self):
        """
        Create some dictionaries for testing.
        """
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_top_students_2(self):
        """
        Test top_student with cs122 dictionary and 2 argument
        """
        self.assertEqual(hw4.top_students(self.cs122, 2), ['Anna', 'Alex'])

    def test_top_students_10(self):
        """
        Test top_student with cs122 dictionary and 10 argument
        """
        self.assertEqual(hw4.top_students(self.cs122, 10), ['Anna',
                                                            'Alex', 'Zoe',
                                                            'Dan'])

    def test_top_students(self):
        """
        Test top_student with cs122 dictionary and no argument
        """
        self.assertEqual(hw4.top_students(self.cs122), ['Anna', 'Alex',
                                                        'Zoe'])

    def test_top_students_empty(self):
        """
        Test top_student with empty dictionary and 6 argument
        """
        self.assertEqual(hw4.top_students(self.empty_class, 6), [])


class TestQ2(unittest.TestCase):
    """
    Test case for the normal execution of the final_grade function
    """

    def setUp(self):
        """
        Create some dictionaries for testing.
        """
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_final_grade(self):
        """
        Test final_grade with cs122 dictionary and no argument
        """
        self.assertEqual(hw4.final_grade(self.cs122), {'Zoe': 91,
                                                       'Alex': 94, 'Dan': 80,
                                                       'Anna': 101})

    def test_final_grade_2(self):
        """
        Test final_grade with cs122 dictionary and 2 argument
        """
        self.assertEqual(hw4.final_grade(self.cs122, 2), {'Zoe': 92,
                                                          'Alex': 95,
                                                          'Dan': 81,
                                                          'Anna': 102})

    def test_final_grade_empty(self):
        """
        Test final_grade with cs122 dictionary and 5 argument
        """
        self.assertEqual(hw4.final_grade(self.empty_class, 5), {})


class TestQ3(unittest.TestCase):
    """
    Test case for the normal execution of the boost_grade function
    """

    def setUp(self):
        """
        Create some dictionaries for testing.
        """
        self.iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                         'Bryan': 2, 'Andrea': 110}
        self.exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95,
                     'Anna': 64, 'Bryan': 95, 'Andrea': 86}

    def test_boost_grade(self):
        """
        Test boost_grade with iclicker and exam dictionary
        """
        self.assertEqual(hw4.boost_grade(self.iclicker, self.exam),
                         {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96,
                          'Ryan': 90, 'Andrea': 87, 'Dan': 89})

    def test_boost_grade_exam(self):
        """
        Test boost_grade with exam and empty dictionary
        """
        self.assertEqual(hw4.boost_grade({}, self.exam),
                         {'Ryan': 89, 'Andrea': 86, 'Bryan': 95,
                          'Anna': 64, 'Dan': 89, 'Alex': 95})

    def test_boost_grade_iclicker(self):
        """
        Test boost_grade with exam and empty dictionary
        """
        self.assertEqual(hw4.boost_grade(self.iclicker, {}),
                         {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0,
                          'Anna': 1, 'Alex': 1})

    def test_boost_grade_empty(self):
        """
        Test boost_grade with two empty dictionary
        """
        self.assertEqual(hw4.boost_grade({}, {}), {})


class TestQ4(unittest.TestCase):
    """
    Test case for the normal execution of the word_lengths function
    """

    def setUp(self):
        self.emptyString = ''
        self.phrase = '''Simple is better than     complex, and flat 
             IS BETTER than nested!?!'''

    def test_word_lengths_empty(self):
        """
        Test word_lengths with empty string
        """
        self.assertEqual(hw4.word_lengths(self.emptyString), {})

    def test_word_lengths_phrase(self):
        """
        Test word_lengths with empty a phrase
        """
        self.assertEqual(hw4.word_lengths(self.phrase),
                         {'simple': 6, 'is': 2, 'better': 6, 'than': 4,
                          'complex': 7, 'and': 3, 'flat': 4, 'nested': 6})


class TestQ5(unittest.TestCase):
    """
    Test case for the normal execution of the geometric_sum function
    """

    def test_geometric_sum_neg_num(self):
        """
        Test geometric_sum with negative number
        """
        self.assertEqual(hw4.geometric_sum(-5), 0)

    def test_geometric_sum_zero(self):
        """
        Test geometric_sum with zero
        """
        self.assertEqual(hw4.geometric_sum(0), 0)

    def test_geometric_sum_num_1(self):
        """
        Test geometric_sum with number 1
        """
        self.assertEqual(hw4.geometric_sum(1), 0.5)

    def test_geometric_sum_num_2(self):
        """
        Test geometric_sum with number 2
        """
        self.assertEqual(hw4.geometric_sum(2), 0.75)

    def test_geometric_sum_num_3(self):
        """
        Test geometric_sum with number 3
        """
        self.assertEqual(hw4.geometric_sum(3), 0.875)

    def test_geometric_sum_num_4(self):
        """
        Test geometric_sum with number 4
        """
        self.assertEqual(hw4.geometric_sum(4), 0.9375)

    def test_geometric_sum_num_30(self):
        """
        Test geometric_sum with number 30
        """
        self.assertEqual(hw4.geometric_sum(30), 0.9999999990686774)


if __name__ == "__main__":
    unittest.main()
