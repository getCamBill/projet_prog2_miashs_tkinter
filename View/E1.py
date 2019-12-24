# ==============================================================================
"""LeapFrog : basic implementation of the LeapFrog puzzle"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # play game with mouse
__date__    = "2018-09-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
class LeapFrog(Win):
  """basic implementation of the LeapFrog puzzle"""
  # ----------------------------------------------------------------------------
  def __init__(self, frog=3):
    """create the main window and pack the widgets"""
    Win.__init__(self, title='LeapFrog', grow=False, op=2, click=self.on_click)
    images = tuple(Image(file="frog%s.gif" % c) for c in '012')
    # --------------------------------------------------------------------------
    self.Pioche = dict({})
    for color in ("M", "B"):
      for shape in ("R", "C"):
        for size in ("G", "P"):
          for dug in (1, 0):
            self.idPiece: str = color + shape + size + str(dug)
            piece: str = color+shape+size+dug
            self.Pioche[self.idPiece] = piece
    # --------------------------------------------------------------------------
    board = Frame(self)
    for n in range(2*frog+1): Label(board, image=images)
    Button(self, text='RESET', command=self.on_reset)
    # --------------------------------------------------------------------------
    self.frog, self.board = frog, board; self.on_reset(); self.loop()
  # ----------------------------------------------------------------------------
  def on_reset(self):
    """callback function for the 'RESET' button"""
    for n, cell in enumerate(self.board): # loop over board cells
      # state : 0 = empty cell, 1 = blue frog, 2 = green frog
      cell.state = 1 if n < self.frog else 2 if n > self.frog else 0
  # ----------------------------------------------------------------------------
  def on_click(self, widget, code, mods):
    """callback function for all mouse click events"""
    if widget.master != self.board or widget.index is None or widget.state == 0:
      return # nothing to do if the mouse click is not on a frog
    board, last, n = self.board, self.board.size-1, widget.index
    if widget.state == 1: # blue frog selected
      if n < last and board[n+1].state == 0: # blue frog can move right
        board[n].state, board[n+1].state = 0, 1 # apply blue frog move
      elif n < last-1 and board[n+2].state == 0: # blue frog can jump right
        board[n].state, board[n+2].state = 0, 1 # apply blue frog jump
    elif widget.state == 2: # green frog selected
      if n > 0 and board[n-1].state == 0: # green frog can move left
        board[n].state, board[n-1].state = 0, 2 # apply green frog move
      elif n > 1 and board[n-2].state == 0: # green frog can jump left
        board[n].state, board[n-2].state = 0, 2 # apply green frog jump
# ==============================================================================
if __name__ == "__main__": # testcode for class 'LeapFrog'
  LeapFrog() # create window with default game parameters: frog=3
# ==============================================================================

