# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s):    Mandeep Pable & Trinh Nguyen
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} image_folder
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            Fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):

    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    Please list ALL the instance variables here
    """

    # Add your class variables if needed here - square size, etc...)

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        # Create the restart button widget
        # Create a canvas widget
        # Create a label widget for the score and end of game messages
        # Create any additional instance variable you need for the game
        pass # take out the pass statement and enter your code


    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        pass  # take out the pass statement and enter your code

    def play(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        pass # take out the pass statement and enter your code

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.



# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.

def main():
    # Retrieve and validate the command line arguments using argparse
    # Instantiate a root window
    # Instantiate a MatchGame object with the correct arguments
    # Enter the main event loop
    pass  # take out the pass statement and enter your code

if __name__ == '__main__':
    main()
    
