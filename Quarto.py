from View.Start import Quarto
from Model.Joueur import Joueur
from tkinter import *

if __name__ == '__main__':

    j1 = Joueur()
    j2 = Joueur()
    fenetre = Tk()
    q = Quarto(fenetre, j1, j2)
    fenetre.mainloop()
