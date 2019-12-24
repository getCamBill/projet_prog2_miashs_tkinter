# ==============================================================================
"""SMILEYS : smileys on a grid"""
# ==============================================================================
from tkinter import *

__author__ = "Christophe Schlick"
__version__ = "1.0"
__date__ = "2015-09-15"
# ==============================================================================
from ezTK import *
from random import randrange


# ------------------------------------------------------------------------------
class Smileys(Win):
    """smileys on a grid"""

    # ----------------------------------------------------------------------------
    def __init__(self):
        """create the main window and pack the widgets"""
        # --------------------------------------------------------------------------
        self.PiecesID = []
        for color in ("M", "B"):
            for shape in ("R", "C"):
                for size in ("G", "P"):
                    for dug in (1, 0):
                        pieceID: str = color + shape + size + str(dug)
                        self.PiecesID.append(pieceID+".png")
        # --------------------------------------------------------------------------
        Win.__init__(self, title='QUARTO sa mère', opad=5)
        ws, cells, cols, rows = {}, {}, 6, 4
        images = [Image(file="%s.png" % n) for n in self.PiecesID]
        # --------------------------------------------------------------------------
        ws[1] = Frame(self)
        ws[11] = Button(ws[1], text='SHUFFLE', width=8,
                        command=lambda: self.cb_button(False))
        ws[12] = Button(ws[1], text='RESET', width=8,
                        command=lambda: self.cb_button(True))
        # --------------------------------------------------------------------------
        ws[2] = Grid(self, cols=cols, rows=rows, opad=2)
        for loop in range(cols * rows):
            col, row = loop % cols, loop // cols
            status = (row + col) % 2  # generate checkerboard pattern for cells
            cells[col, row] = Button(ws[2], image=images[status], text=status)
            cells[col, row].bind('<Button-1>', lambda event, cell=(col, row):
            self.cb_cell(cell, True))  # callback for left click on cell
            cells[col, row].bind('<Button-3>', lambda event, cell=(col, row):
            self.cb_cell(cell, False))  # callback for right click on cell
            cells[col, row].bind('<Enter>', lambda event, cell=(col, row):
            self.cb_mouse(cell, True))  # callback when mouse enters cell
            cells[col, row].bind('<Leave>', lambda event, cell=(col, row):
            self.cb_mouse(cell, False))  # callback when mouse leaves cell
        # --------------------------------------------------------------------------
        self.cells, self.cols, self.rows, self.images = cells, cols, rows, images
        self.loop()

    # ----------------------------------------------------------------------------
    def set_cell(self, cell, status=None):
        """set or swap the smiley on a given cell"""
        cells, images = self.cells, self.images
        if status is None: status = 1 - cells[cell]['text']  # swap cell status
        cells[cell]['text'], cells[cell]['image'] = status, images[status]

    # ----------------------------------------------------------------------------
    def cb_cell(self, cell, flag):
        """callback function for each cell of the board"""
        self.set_cell(cell)
        if flag: self.after(2000, lambda: self.set_cell(cell))

    # ----------------------------------------------------------------------------
    def cb_button(self, flag):
        """callback function for the "SHUFFLE" and the "RESET" button"""
        for loop in range(self.cols * self.rows):
            col, row = loop % self.cols, loop // self.cols
            self.set_cell((col, row), (row + col) % 2 if flag else randrange(2))

    # ----------------------------------------------------------------------------
    def cb_mouse(self, cell, flag):
        """callback function when the mouse enters or leaves the cell"""
        self.cells[cell]['relief'] = SOLID if flag else RAISED


# ==============================================================================
if __name__ == "__main__":  # testcode for class 'Smileys'
    Smileys()
# ==============================================================================
