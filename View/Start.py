# ==============================================================================
import os
from msilib.schema import RadioButton
from tkinter import *
from tkinter import ttk
import time
import threading
from Model.Tablier import Tablier
from Model.Pioche import Pioche
from Model.Joueur import Joueur
from Model.Etat import Etat
from Model.Tour import Tour
from Model.IA import IA_random
from Controller.BDD import *
from functools import partial
from threading import Timer
from View.Ajout_user_view import *
import pygame

from PIL import Image, ImageTk
from random import randrange as rr, random

from View.ezCLI import *

LARGEUR = 500
HAUTEUR = 400


# ------------------------------------------------------------------------------
class Quarto():
    # ----------------------------------------------------------------------------
    def __init__(self, fenetre, joueur1: Joueur = None, joueur2: Joueur = None):
        """

        :param fenetre:
        :param joueur1:
        :param joueur2:
        """
        # --------------------------------------------------------------------------
        self.fenetre = fenetre
        self.fenetre.maxsize(width=1200, height=500)
        self.fenetre.minsize(width=1200, height=500)
        self.fenetre.title("Quarto !! ")

        # --------------------------------------------------------------------------
        self.Tablier: Tablier = Tablier()
        self.Etat: Etat = Etat(self.Tablier)
        self.Pioche: Pioche = Pioche()
        self.Joueur1: Joueur = joueur1
        self.Joueur2: Joueur = joueur2
        # --------------------------------------------------------------------------
        self.aborted: bool = False
        self.ia: bool = False
        self.victoire = False
        # --------------------------------------------------------------------------
        self.pioche_buttonListe = {}
        self.plateau_buttonListe = {}
        self.pieceEnJeux = ""
        # --------------------------------------------------------------------------

        self.game()
        # --------------------------------------------------------------------------

    def game(self):
        # --------------------------------------------------------------------------
        self.n = ttk.Notebook(self.fenetre)  # Création du système d'onglets
        self.n.pack()

        self.o1 = ttk.Frame(self.n, width=200, height=400)  # Ajout de l'onglet 1
        self.o1.pack()

        self.o2 = ttk.Frame(self.n, width=200, height=400)  # Ajout de l'onglet 2
        self.o2.pack()

        self.o3 = ttk.Frame(self.n, width=200, height=400)  # Ajout de l'onglet 2
        self.o3.pack()

        self.n.add(self.o1, text='Quarto')  # Nom de l'onglet 1
        self.n.add(self.o2, text='Joueurs')  # Nom de l'onglet 2
        self.n.add(self.o3, text='Selectionner')  # Nom de l'onglet 2
        # --------------------------------------------------------------------------
        AddUser(self.o2)
        # --------------------------------------------------------------------------
        filename = os.path.relpath('..\\Controller\\UserDatabase.db')
        self.database: str = filename
        self.conn = create_connection(self.database)
        # # --------------------------------------------------------------------------
        self.framePlateau = Frame(self.o1, width=200, height=400, bg="grey")
        self.framePlateau.grid(row=0, column=0, padx=10, pady=5)

        self.framePieces = Frame(self.o1, width=200, height=400, bg="grey")
        self.framePieces.grid(row=0, column=2, padx=10, pady=5)

        self.frameCentre = Frame(self.o1, width=200, height=400)
        self.frameCentre.grid(row=0, column=1, padx=10, pady=5)
        # --------------------------------------------------------------------------
        self.fr1 = Frame(self.o3)
        self.fr1.grid(row=0, column=0)
        self.fr2 = Frame(self.o3)
        self.fr2.grid(row=0, column=1)
        # --------------------------------------------------------------------------
        self.user_name_label = Label(self.fr1, text="Entrer les pseudos des deux Joueurs pour commencer \nSi un "
                                                    "joueur n'est pas dans la base de donnée, il faudra le créer.",
                                     bg="grey", borderwidth=2, relief="groove")
        self.user_name_label.grid(row=0, column=1)
        # --------------------------------------------------------------------------
        self.level = Label(self.fr1, text="Niveau : ").grid(row=5, column=0)
        self.indications = Label(self.fr1, text="Facile : colonne et ligne\n Moyen : Facile + diagonale\nExpert : Moyen + carré").grid(row=5, column=0)
        self.level = IntVar()
        self.l1 = Radiobutton(self.fr1, text="Facile", variable=self.level, value=1).grid(row=5, column=1)
        self.l2 = Radiobutton(self.fr1, text="Moyen", variable=self.level, value=2).grid(row=5, column=2)
        self.l3 = Radiobutton(self.fr1, text="Expert", variable=self.level, value=3).grid(row=5, column=3)
        # --------------------------------------------------------------------------
        self.theme = Label(self.fr1, text="Thème du jeux : ").grid(row=4, column=0)
        self.v = IntVar()
        self.r1 = Radiobutton(self.fr1, text="Classique", variable=self.v, value=1).grid(row=4, column=1)
        self.r2 = Radiobutton(self.fr1, text="Abstrait", variable=self.v, value=2).grid(row=4, column=2)
        # --------------------------------------------------------------------------
        self.imageDir1 = 'Classique\\'
        self.imageDir2 = 'Abstrait\\'
        self.imageDir3 = '2D\\'
        self.sonDir = 'Sons\\'
        # --------------------------------------------------------------------------
        self.user_name = Entry(self.fr1, width=30)
        self.user_name.grid(row=1, column=1, padx=20)
        self.user_name_label = Label(self.fr1, text="Joueur 1")
        self.user_name_label.grid(row=1, column=0)
        # --------------------------------------------------------------------------
        self.user_name2 = Entry(self.fr1, width=30)
        self.user_name2.grid(row=2, column=1, padx=20)
        self.user_name_label2 = Label(self.fr1, text="Joueur 2")
        self.user_name_label2.grid(row=2, column=0)
        # --------------------------------------------------------------------------
        # --------------------------------------------------------------------------
        self.n.select(2)
        # -------------------------------------------------------------------------
        self.submit_btn = Button(self.fr1, text="JOUER")
        self.submit_btn['command'] = lambda user1=self.user_name.get(), user2=self.user_name2.get(): self.submit()
        self.submit_btn.grid(row=3, column=1, padx=10, pady=10)
        # --------------------------------------------------------------------------
        self.fenetre.mainloop()
        # --------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    def submit(self):
        """
        Méthode qui récupère le nom des joueurs.
        Si un champ est vide ou si le joueur n'existe pas dans la bdd on renvoie sur le page
        d'ajout d'utilisateur.
        :return:
        """

        user1 = self.user_name.get()
        user2 = self.user_name2.get()
        listeJ = [ele[1] for ele in select_joueur_by_victory(self.conn)]

        if user1 != "" and user2 != "" and user1 in listeJ and user2 in listeJ:  # si les deux joueurs sont dans la BDD on joue
            self.Joueur1.pseudo = user1
            self.Joueur2.pseudo = user2
            self.Tour: Tour = Tour(user1, user2)
            if user1 == 'IA' or user2 == 'IA':
                self.IA = IA_random(self.Tablier, self.Pioche, self.Tour)
                self.ia = True
            self.new_game()
            self.n.select(0)
        else:  # si au moin un des deux joueur n'y est pas
            self.popup(3)
            self.n.select(1)

    # -------------------------------------------------------------------------
    def quelDirImage(self):
        """
        En fonction du thème choisi par l'user
        :return:
        """
        if int(self.v.get()) == 1:
            return self.imageDir1
        elif int(self.v.get()) == 2:
            return self.imageDir2

    # -------------------------------------------------------------------------
    def createPlateau(self):
        """
        Création du plateau de jeu
        :return:
        """
        try:
            photo = PhotoImage(file=self.quelDirImage() + "Z.png")
            idCases = list(self.Tablier.tablier.keys())
            i: int = 0
            for colonne in range(4):
                for ligne in range(4):
                    id = idCases[i]
                    bt = Button(self.framePlateau, text=id, image=photo)
                    bt.image = photo
                    self.plateau_buttonListe[idCases[i]] = bt
                    bt['command'] = lambda idx=idCases[i], binst=bt: self.chooserCase(binst, idx)
                    bt.grid(row=ligne, column=colonne)
                    i += 1
        except Error as e:
            # print(e)
            pass

    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    def createPioche(self):
        """
        Creation de la pioche
        :return:
        """
        try:
            idPieces = list(self.Pioche.listPieceDispo())
            taille = len(self.Pioche.listPieceDispo())
            pieces = []
            i: int = 0
            for ligne in range(4):
                for colonne in range(4):
                    image = Image.open(self.quelDirImage() + idPieces[i] + ".png")
                    photo = ImageTk.PhotoImage(image)
                    button = Button(self.framePieces, image=photo)
                    button.image = photo
                    self.pioche_buttonListe[idPieces[i]] = button
                    button['command'] = lambda idx=idPieces[i], binst=button: self.choixPiece(idx, binst)
                    button.grid(row=ligne, column=colonne)
                    i += 1
        except Error as e:
            # print(e)
            pass

    # --------------------------------------------------------------------------
    def choixPiece(self, idxPiece, binst):
        """

        :param idxPiece:
        :param binst:
        :return:
        """
        try:
            self.aQuiLeTour['text'] = str(
                self.Tour.auTourDe()[1] + " choose la case")  # on actualise pour indiquer quel joueur choisi la case
            self.pieceEnJeux = idxPiece  # on met en variable globale la pièce jouée pour l'afficher dans le label central
            photo = PhotoImage(file=self.quelDirImage() + idxPiece + ".png")
            self.pieceStby.image = photo
            self.pieceStby['image'] = photo  # on garde en référence l'image du bouton
            self.Tablier.piecePourAdversaire(idxPiece, self.Joueur2)
            binst.destroy()
            del self.pioche_buttonListe[idxPiece]

            self.suspens()

            self.disable_normalPiece(1)
            self.Tour.tour += 1

            self.is_IA_turn()
        except Error as e:
            # print(e)
            pass

    # ---------------------------------------------------------------------------
    def chooserCase(self, binst, idxCase):
        """

        :param binst:
        :param idxCase:
        :return:
        """
        try:
            # --------------------------------------------------------------------------
            self.aQuiLeTour['text'] = str(self.Tour.auTourDe()[0] + " choose la pièce")
            self.aQuiLeTour.grid(row=6, column=0)
            self.wait_song.stop()
            if self.Tablier.poserPiece(self.Joueur2, idxCase, self.Pioche) == 1:
                self.popup(1) # si le joueur clique sur un bouton déjà occupé on lui indique de ne pas jouer
            else:
                # -------------
                replace = self.pieceEnJeux  # on récupère la pièce pour l'afficher
                photo = PhotoImage(file=self.quelDirImage() + replace + "R.png")
                # -------------
                binst.image = photo
                binst['image'] = photo  # on garde en référence l'image du bouton
                self.move_song.play()
                photo = PhotoImage(file=self.quelDirImage() + "start.png")
                photoimage = photo.subsample(3, 3)
                self.pieceStby.image = photoimage
                self.pieceStby['image'] = photoimage  # on garde en référence l'image du bouton
                # self.IA.mirror[idxCase] = replace # onnmet la piece dans le plateau mirroir pour IA
                self.idxCase = idxCase
                del self.plateau_buttonListe[idxCase]

            if self.Tour.tour > 2:  # au bout de trois tours on appel la méthode vict
                self.vict()
            self.disable_normalPiece(
                -1)  # on désactive la pioche de bouton pour ne pas ajouter deux fois une même piece
        except Error as e:
            # print(e)
            pass

    # --------------------------------------------------------------------------
    def is_IA_turn(self):

        if self.Tour.auTourDe()[0] == 'IA':
            idcase, boutonPlateau = self.IA.bestPlace(self.plateau_buttonListe)
            self.chooserCase(boutonPlateau, idcase)

            idPiece, boutonPiece = self.IA.worstPiece(self.pioche_buttonListe)
            self.choixPiece(idPiece, boutonPiece)

    # --------------------------------------------------------------------------
    def disable_normalPiece(self, machin):
        """
        On desactive le choix des boutons des pieces dispo
        :param machin:
        :return:
        """
        if machin == 1:
            for btn in self.pioche_buttonListe.values():
                btn['state'] = 'disabled'
        else:
            for btn in self.pioche_buttonListe.values():
                btn['state'] = 'normal'

    # --------------------------------------------------------------------------
    def vict(self):
        """
        Méthode qui call la méthode isQuarto de la classe tablier
        Si Quarto on arrete le jeu et on lance une animation
        :return:
        """
        if self.Tablier.isQuarto(self.level.get()):
            self.victoire = True
            self.aQuiLeTour['text'] = ""
            self.win['text'] = "QUARTO !!! " + self.Tour.auTourDe()[0] + " a gagné la partie"
            update_partie_joueur(self.conn,
                                 (1, 0, self.Tour.auTourDe()[0]))  # on met à jour les données de chaque partie
            update_partie_joueur(self.conn, (0, 1, self.Tour.auTourDe()[1]))
            self.mon_audio.play()
            self.popup(2)
        elif self.Pioche.listPieceDispo() == 0:
            self.popup(4)

    # --------------------------------------------------------------------------
    def popup(self, code):
        """

        :param code:
        :return:
        """
        self.fInfos = Toplevel()  # Popup -> Toplevel()
        # self.fInfos.
        # ----------------------------------------------------
        if code == 1:
            self.fInfos.title('Infos')
            Button(self.fInfos, text='La case est déjà occupée !', command=self.fInfos.destroy).pack(padx=10, pady=10)
        # ----------------------------------------------------
        elif code == 2:
            self.fInfos.title('Infos')
            # button = Button(self.fInfos, text='Nouvelle partie').pack(padx=10, pady=10)
            # button['command'] = lambda order=None: self.game()
            Button(self.fInfos, text='Quitter', command=self.fenetre.destroy).pack(padx=10, pady=10)
        # ----------------------------------------------------
        elif code == 3:
            self.fInfos.title('Infos')
            Label(self.fInfos,
                  text='Un des deux joueurs n\'est pas dans la BDD \n veuillez renseigner le pseudo.').pack(padx=10,
                                                                                                            pady=10)
            Button(self.fInfos, text='OK', command=self.fInfos.destroy).pack(padx=10, pady=10)
        # ----------------------------------------------------
        elif code == 4:
            self.fInfos.title('Fin')
            Label(self.fInfos, text="Plus de pièces disponible donc fin de la partie !")
            Button(self.fInfos, text='Quitter', command=self.fenetre.destroy).pack(padx=10, pady=10)
        # ----------------------------------------------------
        self.fInfos.transient(self.fenetre)  # Réduction popup impossible
        self.fInfos.grab_set()  # Interaction avec fenetre jeu impossible
        self.fenetre.wait_window(self.fInfos)  # Arrêt script principal

    # --------------------------------------------------------------------------
    def suspens(self):
        self.wait_song.set_volume(10)
        self.wait_song.play(0, 5000)

    # --------------------------------------------------------------------------
    def new_game(self):
        """

        :return:
        """
        photo = PhotoImage(file=self.quelDirImage() + "start.png")
        photoimage = photo.subsample(3, 3)
        self.pieceStby = Label(self.frameCentre, image=photoimage)
        self.pieceStby.image = photoimage
        self.pieceStby.grid(row=4, column=0)
        # --------------------------------------------------------------------------
        self.win = Label(self.frameCentre, text=' ... ', font=("Courier", 15, 'bold'))
        self.win.grid(row=5, column=0)
        # --------------------------------------------------------------------------
        self.createPioche()
        self.createPlateau()
        self.cases: list = []
        self.idxCase = ''
        # --------------------------------------------------------------------------
        self.aQuiLeTour = Label(self.frameCentre, text=str(self.Tour.auTourDe()[0] + " \nchoose la pièce"),
                                font=("Courier", 15, 'bold'))
        self.aQuiLeTour.grid(row=6, column=0)
        # --------------------------------------------------------------------------
        pygame.mixer.init()
        self.mon_audio = pygame.mixer.Sound(self.sonDir + "clap.wav")
        self.move_song = pygame.mixer.Sound(self.sonDir + "351518__mh2o__chess-move-on-alabaster.wav")
        self.wait_song = pygame.mixer.Sound(self.sonDir + "0218.wav")
        # --------------------------------------------------------------------------
# ==============================================================================
if __name__ == '__main__':
    code="""
    j1 = Joueur()
    j2 = Joueur()
    fenetre = Tk()
    Quarto(fenetre, j1, j2)
    fenetre.mainloop()
    """;testcode(code)
# ==============================================================================
