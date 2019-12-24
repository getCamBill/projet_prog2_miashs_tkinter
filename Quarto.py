from View.gameClass import Game
from View.A import *
from Model.Joueur import *
from tkinter import *

if __name__ == "__main__":
    # first()
    j1 = Joueur('A')
    j2 = Joueur('B')
    g = Game(j1, j2)
    g.start()
