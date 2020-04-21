# ----------------------------------------------------------------------
# Name:        tagdemo
# Purpose:     demonstrate the use of tags
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Demonstrate the use of Canvas tags.

The user clicks on one or more shapes to select them.
When the GO button is pressed, the selected shapes move to the right.
"""
import tkinter


class TagDemo:

    """
    class to demonstrate the use of tags.

    Argument:
    parent: (tkinter.Tk) the root window object

    Attributes:
    canvas: (tkinter.Canvas) A Canvas widget
    """

    def __init__(self, parent):
        parent.title('CS 122')
        self.parent = parent
        # create a GO button and associate it with the go method
        start_button = tkinter.Button(parent, text='GO', width=20,
                                      command=self.go)
        start_button.grid()  # register it with a geometry manager

        # create a Canvas widget
        self.canvas = tkinter.Canvas(parent, width=500, height=200,
                                     background='lawn green')
        # Create some shapes
        for count in range(10, 180, 20):
            self.canvas.create_oval(10, 10+count,
                                    20, 20+count,
                                    fill="red")
        # bind a click on the Canvas to the select method.
        self.canvas.bind("<Button-1>", self.select)
        self.canvas.grid()

    def select(self, event):
        """
        Tag the clicked circle  as 'selected'.
        :param event (tkinter.Event)
        :return: None
        """
        shape = self.canvas.find_withtag(tkinter.CURRENT)
        self.canvas.itemconfigure(shape, tag="selected")

    def go(self):
        """
        Move all circles that have been tagged "selected" 10
        pixels to the right.
        :return:
        """
        for each_shape in self.canvas.find_withtag("selected"):
            self.canvas.move(each_shape, 10, 0)


def main():
    root = tkinter.Tk()  # create the GUI application main window
    tag_app = TagDemo(root)
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
