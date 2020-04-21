# ----------------------------------------------------------------------
# Name:        makingsoup
# Purpose:     Demonstrate using Beautiful Soup to parse html files
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in the Beautiful Soup lecture.

Demonstrate using Beautiful Soup to parse html files.
"""
import bs4


def make_soup(filename):
    """
    Parse the html file specified.
    :param filename: string - name of the html file to be parsed
    :return: BeautifulSoup object
    """
    with open(filename, 'r', encoding='utf-8') as html_file:
        soup = bs4.BeautifulSoup(html_file, "html.parser")
    return soup


def taste(soup):
    """
    Explore the given Beautiful soup object.
    :param soup: BeautifulSoup object
    :return: None
    """
    # Your code here


def main():
    soup = make_soup("demosoup.html")
    taste(soup)


if __name__ == "__main__":
    main()
