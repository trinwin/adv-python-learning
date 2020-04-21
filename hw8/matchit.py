# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s):   Mandeep Pabla & Trinh Nguyen
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
import sys


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
    num_of_row = 4
    num_of_col = 4
    num_of_tile = num_of_row * num_of_col
    num_of_tries = 0
    max_free_tries = 13
    score = 100
    delay_ms = 0
    first_image_id = ""
    second_image_id = ""
    first_tile_id = ""
    second_tile_id = ""
    score_label = ""
    parent = ""
    match_tile_tag = "match_tile"
    image_tag = "image"
    tile_starter_color = "yellow"
    game_over_label = ""
    num_try_label = ""

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        self.parent = parent
        self.player_color = player_color

        if delay:
            self.delay_ms = 1000
        else:
            self.delay_ms = 3000

        self.folder_images = [i for i in os.listdir(folder)
                              if i.endswith(".gif")]
        self.image_names = 2 * self.folder_images
        random.shuffle(self.image_names)

        # Dictionary that maps each image name
        self.image_dict = {}
        for image in self.folder_images:
            self.image_dict[image] = tkinter.PhotoImage(
                file=(folder + '/' + image))

        restart_button = tkinter.Button(parent, text='RESTART', width=20,
                                        command=self.restart)
        restart_button.grid(column=0, row=1)

        self.score_label = tkinter.Label(parent, text='score: 100')

        # Instantiate our Canvas widget with the root as parent
        self.canvas = tkinter.Canvas(parent, width=500, height=500)

        # Draw the tiles and images associated with the tiles
        tag_num = self.num_of_tile
        for column in range(self.num_of_row):
            for row in range(self.num_of_col):
                width1 = column * 125
                height1 = row * 120
                width2 = width1 + 125
                height2 = height1 + 120
                tag_num -= 1
                tile_tag = 'tile' + str(self.num_of_tile - tag_num)
                self.canvas.create_rectangle(width1, height1, width2,
                                             height2,
                                             fill=self.tile_starter_color,
                                             outline=player_color,
                                             tag=(tile_tag))
                self.canvas.create_image(
                    width1+125/2, height1+120/2, image=self.image_dict
                    [self.image_names[self.num_of_tile - tag_num - 1]],
                    tag=(tile_tag, self.image_tag),
                    state=tkinter.HIDDEN)

        self.canvas.bind("<Button-1>", self.play)
        self.canvas.grid()
        self.score_label.grid(column=0, row=290)

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        # check if player has started the game
        if self.num_of_tries == 0 and not self.first_tile_id:
            return

        # change color of all matched tiles
        for match_tile in self.canvas.find_withtag(self.match_tile_tag):
            self.canvas.itemconfigure(match_tile,
                                      fill=self.tile_starter_color)
        # delete all images
        for image in self.canvas.find_withtag(self.image_tag):
            self.canvas.delete(image)
        # reset score
        self.score = 100
        self.score_label['text'] = 'score: 100'
        self.num_of_tries = 0
        self.first_tile_id = self.first_image_id = ""
        self.second_tile_id = self.second_image_id = ""

        # Delete game over label and number of tries label if exist
        if self.game_over_label or self.num_try_label:
            self.game_over_label.destroy()
            self.num_try_label.destroy()

        # Reshuffle images
        random.shuffle(self.image_names)

        # Recreate images
        for i in range(1, 17):
            tile_tag = "tile" + str(i)
            tile_id = self.canvas.find_withtag(tile_tag)
            self.canvas.itemconfigure(tile_id, tag=tile_tag)
            tile_coords = self.canvas.coords(tile_id)
            self.canvas.create_image(
                tile_coords[0]+125/2, tile_coords[1]+120/2,
                image=self.image_dict[self.image_names[i-1]],
                tag=(tile_tag, self.image_tag),
                state=tkinter.HIDDEN)

    def play(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        curr_obj_id = self.canvas.find_withtag(tkinter.CURRENT)
        # Check to make sure player selects a tile object or others
        if not curr_obj_id:
            return

        tile_id = curr_obj_id[0]
        # check if player reselect the image
        if self.image_tag in self.canvas.gettags(tile_id):
            return

        tile_color = self.canvas.itemcget(tile_id, "fill")

        # Check if player clicks on tile that has been previously matched
        # or if player clicks on the same tile twice
        if tile_color == self.player_color or self.first_tile_id == tile_id:
            return

        # Check if player clicks on a tile while two images are revealed
        if self.first_tile_id and self.second_tile_id:
            return

        tile_tags = self.canvas.gettags(tile_id)
        image_id = self.canvas.find_withtag(tile_tags[0])[1]
        self.canvas.itemconfigure(image_id, state=tkinter.NORMAL)

        if not self.first_image_id:  # Get the first tile
            self.first_image_id = image_id
            self.first_tile_id = tile_id
        else:                       # Get the second tile
            self.second_image_id = image_id
            self.second_tile_id = tile_id
            first_image_name = self.canvas.itemcget(self.first_image_id,
                                                    self.image_tag)
            second_image_name = self.canvas.itemcget(self.second_image_id,
                                                     self.image_tag)
            if first_image_name == second_image_name:
                self.canvas.after(self.delay_ms, self.match)
            else:
                self.canvas.after(self.delay_ms, self.add_one_try)

    def match(self):
        """
        This method is invoked when 2 tiles are matched
        :return: None
        """
        self.canvas.itemconfigure(self.first_tile_id, fill=self.player_color)
        self.canvas.addtag_withtag(self.match_tile_tag, self.first_tile_id)
        self.canvas.itemconfigure(self.second_tile_id, fill=self.player_color)
        self.canvas.addtag_withtag(self.match_tile_tag, self.second_tile_id)
        self.add_one_try()

    def add_one_try(self):
        """
        This method is invoked when user complete one try
        :return: None
        """
        self.canvas.itemconfigure(self.first_image_id, state=tkinter.HIDDEN)
        self.canvas.itemconfigure(self.second_image_id, state=tkinter.HIDDEN)
        self.first_image_id = self.second_image_id = ""
        self.first_tile_id = self.second_tile_id = ""
        self.num_of_tries += 1
        if self.num_of_tries > self.max_free_tries:
            self.score -= 10
            new_score = 'score: ' + str(self.score)
            self.score_label['text'] = new_score

        if self.num_of_tries >= 8:
            if len(self.canvas.find_withtag(self.match_tile_tag)) == 16:
                self.game_over()

    def game_over(self):
        """
        This method is invoked when the game is finished
        :return: None
        """
        self.game_over_label = tkinter.Label(self.parent, text="Game over!")
        num_tries_text = "Number of tries: " + str(self.num_of_tries)
        self.num_try_label = tkinter.Label(self.parent, text=num_tries_text)
        self.game_over_label.grid(column=0, row=280)
        self.num_try_label.grid(column=0, row=300)


def valid_folder(folder):
    """
    Validate the folder command line argument
    :param folder: folder name
    :return: folder
    """
    if not os.path.isdir(folder):
        raise argparse.ArgumentTypeError("argument image_folder: {} is "
                                         "not a valid folder".format(folder))
    else:
        gif_list = [i for i in os.listdir(folder) if i.endswith(".gif")]
        if len(gif_list) != 8:
            raise argparse.ArgumentTypeError("argument image_folder: "
                                             "fewer images must contain "
                                             "at least 8 gif images")
    return folder


def get_arguments():
    """
    Parse the command line arguments.
    :return color (string): color of match tile user chose
    :return image_folder (string): name of image folder
    :return fast (boolean): fast option
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What color would you like for the player?',
                        choices=['blue', 'green', 'magenta'])

    parser.add_argument('image_folder',
                        help='What folder contains the game images?',
                        action='store',
                        type=valid_folder)

    parser.add_argument('-f', '--fast',
                        help='Fast or slow game?',
                        action='store_true')

    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast

    return color, image_folder, fast


def main():
    # Retrieve and validate the command line arguments using argparse
    color, image_folder, fast = get_arguments()
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a MatchGame object with the correct arguments
    MatchGame(root, color, image_folder, fast)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
