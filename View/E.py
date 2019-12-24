# ==============================================================================
"""PILLOW : demo program for the Pillow module"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2018-10-15"
# ==============================================================================
from tkinter import *
from Model.Tablier import Tablier
from Model.Pioche import Pioche
from Model.Joueur import Joueur
from Model.Etat import Etat
from Model.Tour import Tour
from Controller.BDD import *
from functools import partial
import tkinter as tk
from PIL import Image, ImageTk
from random import randrange as rr

# ------------------------------------------------------------------------------
class Quarto():
  """demo program for the Pillow module"""
  LARGEUR = 500
  HAUTEUR = 400
  # ----------------------------------------------------------------------------
  def __init__(self, joueur1: Joueur = None, joueur2: Joueur = None):
    """create the main window and pack the widgets"""

    self.database: str = 'C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db'
    self.conn = create_connection(self.database)

    self.Etat: Etat = Etat()
    self.Tablier: Tablier = Tablier()
    self.Pioche: Pioche = Pioche()
    self.Joueur1: Joueur = joueur1
    self.Joueur2: Joueur = joueur2
    self.Tour: Tour = Tour()
    self.aborted: bool = False

    self.fenetre = tk.Tk()
    self.fenetre.title("Quarto !! ")

    self.canvas = Canvas(self.fenetre, width=300, height=300)
    self.canvas.pack()

    # self.frameGauche = tk.Frame(self.fenetre, width=400, height=400)
    # self.frameGauche.grid(row=0,column=0, padx=10, pady=5)

    # -------------------------------------------------------------------------
    def button_click_exit_mainloop(event):
      event.widget.quit()  # this will cause mainloop to unblock.
     # C:Users\camil\PycharmProjects\UI\

    for i, piece in enumerate(self.Pioche.listPieceDispo()):
    #   k = 0
    #   for i in range(4):
    #     for j in range(4):
      # photo = PhotoImage(file=r"%s.png" % piece)
      # photoimage = photo.subsample(1, 1)
      # Button(self.fenetre, image=photoimage)
      #   piece = self.Pioche.listPieceDispo()[k]
        image = Image.open(piece+".png")
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.image = photo  # keep a reference!
        label.pack()
        # label.grid(column=i, row=j)
        # k += 1
    self.fenetre.mainloop()
    # --------------------------------------------------------------------------


if __name__ == '__main__':
  Quarto()

# ==============================================================================

