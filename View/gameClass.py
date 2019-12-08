from Model.Tablier import Tablier
from Model.Pioche import Pioche
from Model.Joueur import Joueur
from Model.Etat import Etat
from Model.Tour import Tour


class Game(object):

    def __init__(self):
        self.Etat = Etat()
        self.Tablier = Tablier()
        self.Pioche = Pioche()
        self.Joueur1 = Joueur()
        self.Joueur2 = Joueur()
        self.Tour = Tour()
        self.aborted = False

    def isAborted(self, input):
        if input == "quitter" or "q" or "QUITTER" or "Q":
            self.aborted = True
            print("Partie ABORTED !!")
        else:
            return input

    def showRules(self):
        print("--------------------------------------------------")
        print("-------BIENVENUE DANS LE JEU DU QUARTO !!!--------")
        print("--------------------------------------------------")
        print("PRESENTATION ET PREPARATION '\n' \
        - Un plateau de 16 cases'\n' \
        -16 pièces différentes ayant chacune 4 caractères :'\n' \
        Beige ou Marron, Ronde ou Carrée, Grande ou Petite, pleine ou creuse.'\n' \
        En début de partie, les pièces sont déposées à côté du plateau.")

        print("BUT DU JEU '\n' \
        Créer sur le plateau un alignement de 4 pièces ayant au moins un caractère commun.'\n' \
        Cet alignement peut-être horizontal, vertical ou diagonal")

        print("DEROULEMENT D’UNE PARTIE'\n' \
        - Le premier joueur est tiré au sort.'\n' \
        - Il choisit une des 16 pièces et la donne à son adversaire.'\n' \
        - Celui-ci doit la placer sur une des cases du plateau et choisir '\n' \
        ensuite une des 15 pièces restantes pour la donner à son adversaire. '\n' \
        - A son tour, celui-ci la place sur une case libre et ainsi de suite...")

        print("GAIN DE LA PARTIE'\n' \
        La partie est gagnée par le premier joueur qui annonce “QUARTO !”.'\n' \
        1 Un joueur fait “QUARTO !” et gagne la partie lorsque, en plaçant la pièce donnée:'\n' \
        -> Il crée une ligne de 4 claires ou 4 foncées ou 4 rondes ou 4 carrées ou 4 hautes ou 4 basses ou 4 pleines ou 4 creuses.'\n' \
        Plusieurs caractères peuvent se cumuler.'\n' \
        -> Il n’est pas obligé d’avoir lui même déposé les trois autres pièces.'\n' \
        -> Il doit faire reconnaître sa victoire en annonçant “QUARTO !”.'\n' \
        2 Si ce joueur n’a pas vu l’alignement et donne une pièce à l’adversaire:'\n' \
        -> Ce dernier peut “à ce moment” annoncer “QUARTO !”, et montrer l’alignement: c’est lui qui gagne la partie.'\n' \
        3 Si aucun des joueurs ne voit l’alignement durant le tour de jeu où il se crée, cet alignement perd toute sa valeur et la partie suit son cours.")
        print("FIN DE LA PARTIE '\n' \
        - Victoire: un joueur annonce et montre un “QUARTO !”. '\n'\
        - Egalité: toutes les pièces ont été posées sans vainqueur.")

    def actionPiece(self):

        print("Le joueur 1 choisit une pièce pour le joueur 2, dans la liste suivante : \n")
        self.Pioche.showPieces()

        piece = input("Id de la pièce choisis : ")
        self.Tablier.piecePourAdversaire(piece, self.Joueur2)

    def actionCase(self):
        print("Le joueur 2 indique la case : ")
        self.Tablier.showTablier()

        case = input("Id de la case : ")
        self.Tablier.poserPiece(self.Joueur2, case, self.Pioche)
    def start(self):
        self.showRules()
        self.aborted = False

        j: str = ""
        i: int = 0
        while not self.aborted:

            if i % 2 == 0:  # un tour sur deux un joueur peux jouer
                self.Joueur2.jouer = True
                self.Joueur1.jouer = False
                joueur: str = "Joueur 2"
                donneur: str = "Joueur 1"
            else:
                self.Joueur1.jouer = True
                self.Joueur2.jouer = False
                joueur: str = "Joueur 1"
                donneur: str = "Joueur 2"

            print("Le joueur {0} choisit une pièce pour l'adversaire, dans la liste suivante : \n".format(donneur))
            self.Pioche.showPieces()

            piece = input("Id de la pièce choisis : ")

            self.Tablier.piecePourAdversaire(piece, self.Joueur2)
            print("Le joueur {0} indique la case : ".format(joueur))
            self.Tablier.showTablier()

            case = input("Id de la case : ")

            self.Tablier.poserPiece(self.Joueur2, case, self.Pioche)
            i += 1
            if i > 3: # on appelle les fonctions seulement au bout de 4 tours
                if self.Tablier.isDiagoQuarto() or \
                self.Tablier.isLigneQuarto() or \
                self.Tablier.isColonneQuarto():
                    print("QUARTO !! \n    FIN DE LA PARTIE ......")
                    print("{0} à gagné face à {1}".format(joueur, donneur))
                    self.aborted = True
