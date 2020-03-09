# ----------------------------------------------------------------------
# Name:        book
# Purpose:     Demonstrate the use of __getitem__ and __len__
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing a Book class definition.

Implement __getitem__ to access individual chapters.
Implement __len__ to return the number of chapters.
"""


class Book(object):
    
    """
    Represent a book

    Arguments:
    author (string): the author's name
    title (string): the book title

    Attributes:
    author (string): the author's name
    title (string): the book title
    content (list):  list containing the content of each chapter
    """

    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.content = []

    def __str__(self):
        description = [f'{self.title} by: {self.author}']
        chapter_number = 1
        # add chapter numbers to the representation
        for chapter in self.content:
            description.append(f'Chapter {chapter_number}\n{chapter}')
            chapter_number += 1
        return '\n'.join(description)

    def __getitem__(self, key):
        # if the index is in the existing chapters range
        if 0 < key <= len(self.content):
            return self.content[key - 1]  # convert to 0 based indexing

    def __len__(self):
        return len(self.content)  # return the number of chapters

    def add_chapter(self, text):
        """
        Add the given text as a new chapter at the end of the book.
        :param text: (string) - the content of the chapter to be added
        :return: None
        """
        self.content.append(text)
