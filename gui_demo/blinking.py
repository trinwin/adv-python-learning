# ----------------------------------------------------------------------
# Name:        blinking
# Purpose:     Demonstrate the use of after
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to implement a simple blinking app

The Spartan image appears and disappears
"""
import tkinter


class BlinkApp:
    
    """
    GUI App class for a blinking Spartan.

    Argument:
    parent (tkinter.Tk): the root window object

    Attribute:
    canvas (tkinter.Canvas): Home to the blinking Spartan
    sammy (PhotoImage): Spartan image
    image_id (integer):  ID of the Canvas image object
    """

    def __init__(self, parent):
        parent.title("CS 122")
        # instantiate our Canvas widget with the root as parent
        self.canvas = tkinter.Canvas(parent, width=300,
                                     height=300,
                                     background = 'yellow')
        self.sammy = tkinter.PhotoImage(file='Sammy.gif')
        self.image_id = self.canvas.create_image(150, 150, image=self.sammy)
        self.canvas.grid()

        self.canvas.after(1000, self.disappear)

        print('A')

    def disappear(self):
        """
        Remove Sammy's image from the Canvas
        Call appear to have the image reappear after a delay
        :return: None
        """
        self.canvas.delete(self.image_id)
        self.canvas.after(1000, self.appear)

        print('B')

    def appear(self):
        """
        Add Sammy's image to Canvas
        Call disappear to have the image disappear after a delay
        :return: None
        """
        print('C')
        # self.image_id = self.canvas.create_image(150, 150, image=self.sammy)
        # self.canvas.after(1000, self.disappear)


def main():
    # create the GUI application main window
    root = tkinter.Tk()
    # Instantiate our app object
    painting = BlinkApp(root)
    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
