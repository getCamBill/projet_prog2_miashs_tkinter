# ==============================================================================
from tkinter import *
from Model.Tablier import Tablier
from Model.Pioche import Pioche
from Model.Joueur import Joueur
from Model.Etat import Etat
from Model.Tour import Tour
from Controller.BDD import *
from functools import partial
from threading import Timer
import pygame
from PIL import Image, ImageTk
from random import randrange as rr, random
LARGEUR = 500
HAUTEUR = 400
# ------------------------------------------------------------------------------
class Quarto():

    # ----------------------------------------------------------------------------
    def __init__(self, fenetre, joueur1: Joueur = None, joueur2: Joueur = None):
        self.database: str = 'C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db'
        self.conn = create_connection(self.database)
        # --------------------------------------------------------------------------
        self.Tablier: Tablier = Tablier()
        self.Etat: Etat = Etat(self.Tablier)
        self.Pioche: Pioche = Pioche()
        self.Joueur1: Joueur = joueur1
        self.Joueur2: Joueur = joueur2
        self.Tour: Tour = Tour()
        self.aborted: bool = False
        """create the main window and pack the widgets"""
        # --------------------------------------------------------------------------
        self.fenetre = fenetre
        self.fenetre.title("Quarto !! ")
        # --------------------------------------------------------------------------
        self.framePlateau = Frame(self.fenetre, width=200, height=400, bg="grey")
        self.framePlateau.grid(row=0, column=0, padx=10, pady=5)

        self.framePieces = Frame(self.fenetre, width=200, height=400, bg="grey")
        self.framePieces.grid(row=0, column=2, padx=10, pady=5)

        self.frameCentre = Frame(self.fenetre, width=200, height=400)
        self.frameCentre.grid(row=0, column=1, padx=10, pady=5)
        # --------------------------------------------------------------------------
        self.new_game()
        # --------------------------------------------------------------------------
        self.fenetre.mainloop()
        # --------------------------------------------------------------------------
        # -------------------------------------------------------------------------

    def createPlateau(self):
        photo = PhotoImage(file=r"Z.png")  # C:Users\camil\PycharmProjects\UI\
        photoimage = photo.subsample(1, 1)
        idCases = list(self.Tablier.tablier.keys())
        # print(idCases)
        i: int = 0
        for ligne in range(4):
            for colonne in range(4):
                # bt = Button(self.framePlateau, image=photoimage)
                id = idCases[i]
                bt = Button(self.framePlateau, text=id, width=5, height=5)
                bt['command'] = lambda idx=idCases[i], binst=bt: self.choisirCase(binst, idx)
                bt.grid(row=ligne, column=colonne)
                # bt.pack()
                i += 1

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

    def createPioche(self):
        idPieces = list(self.Pioche.listPieceDispo())
        taille = len(self.Pioche.listPieceDispo())
        # print(idPieces)
        pieces = []
        i: int = 0
        for ligne in range(4):
            for colonne in range(4):
        # for i, piece in enumerate(self.Pioche.listPieceDispo()):
                image = Image.open(idPieces[i] + ".png")
                photo = ImageTk.PhotoImage(image)
                button = Button(self.framePieces, text=idPieces[i], width=5, height=5)
                # self.button['image'] = photo
                button['command'] = lambda idx=idPieces[i], binst=button: self.choixPiece(idx, binst)
                button.grid(row=ligne, column=colonne)
                # button.pack(side="bottom", fill="both", expand="yes")
                i += 1
# --------------------------------------------------------------------------

    def choixPiece(self, idxPiece, binst):
        print(idxPiece)
        self.pieceStby['text'] = idxPiece
        self.Tablier.piecePourAdversaire(idxPiece, self.Joueur2)
        binst.destroy()

# ----------------------------------------------------------------------------
    def show(self):
        print("Tablier : ")
        print(self.Tablier.tablier)
        print("Pioche : ")
        print(self.Pioche.Pioche)

# ----------------------------------------------------------------------------
    def choisirCase(self, binst, idxCase):
        print(idxCase)
        self.idxCase = idxCase
        binst['text'] = self.pieceStby['text']
        if self.Tablier.poserPiece(self.Joueur2, idxCase, self.Pioche) == 1:
            self.popup(1)

        if self.Tour.tour > 2:
            self.vict()
        self.Tour.tour += 1
# --------------------------------------------------------------------------
    def vict(self):
        # on appelle les fonctions seulement au bout de 4 tours
        if self.Tablier.isDiagoQuarto() or \
                self.Tablier.isLigneQuarto() or \
                self.Tablier.isColonneQuarto():
            self.victoire = True
            self.win['text'] = "QUARTO !!! "
            self.mon_audio.play(-1)
            self.popup(2)
# --------------------------------------------------------------------------
    def popup(self, code):
        fInfos = Toplevel()  # Popup -> Toplevel()
        if code == 1:
            fInfos.title('Infos')
            Button(fInfos, text='Ok je fais pas le teubé...', command=fInfos.destroy).pack(padx=10, pady=10)
        elif code == 2:
            fInfos.title('Infos')
            Button(fInfos, text='Nouvelle partie', command=self.new_game).pack(padx=10, pady=10)
            Button(fInfos, text='Quitter', command=self.fenetre.destroy).pack(padx=10, pady=10)

        fInfos.transient(self.fenetre)  # Réduction popup impossible
        fInfos.grab_set()  # Interaction avec fenetre jeu impossible
        self.fenetre.wait_window(fInfos)  # Arrêt script principal

# --------------------------------------------------------------------------

    def new_game(self):

        # photo = PhotoImage(file=r"Z.png")
        self.pieceStby = Label(self.frameCentre, text='test')
        # self.pieceStby.grid(row=1, column=1)
        self.pieceStby.pack()
        # --------------------------------------------------------------------------
        self.win = Label(self.frameCentre, text=' ... ')
        # self.pieceStby.grid(row=1, column=1)
        self.win.pack()
        # --------------------------------------------------------------------------
        self.aQuiLeTour = Label(self.frameCentre, text='au tour de ...')
        self.aQuiLeTour.pack()
        # --------------------------------------------------------------------------
        self.createPioche()
        self.createPlateau()
        self.cases: list = []
        self.idxCase = ''
        # --------------------------------------------------------------------------
        pygame.mixer.init()
        self.mon_audio = pygame.mixer.Sound("clap.wav")
        # --------------------------------------------------------------------------
        self.mon_audio.stop()
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ==============================================================================
if __name__ == '__main__':
    j1 = Joueur('A')
    j2 = Joueur('B')
    fenetre = Tk()
    q = Quarto(fenetre, j1, j2)
    fenetre.mainloop()
    # q.show()
# ==============================================================================
