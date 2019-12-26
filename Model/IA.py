"""
Classe IA:
Jouer contre l'ordi
"""

from Model.Tablier import Pioche, Tablier
from Model.Pioche import Pioche
from Model.Tour import Tour
from Model.Joueur import Joueur
import random
# ==============================================================================
class IA_random(object):

    def __init__(self, Tablier: Tablier = None, Pioche: Pioche = None, Tour: Tour = None):
        self.tablier = Tablier
        self.pieces = Pioche
        self.tour = Tour.tour
# --------------------------------------------------------------------------
    def casesDispo(self):
        casesDispo: list = []
        for case in self.tablier.tablier.items():
            if not case[1]:
                casesDispo.append(case[0])
        return casesDispo
# --------------------------------------------------------------------------
    def piecesDispo(self):
        piecesDispo: list = []
        for piece in self.pieces.Pioche.keys():
            piecesDispo.append(piece)
        return piecesDispo
# --------------------------------------------------------------------------
    def nextCoupWin(self, piece):
        pass
# --------------------------------------------------------------------------
    def nextCoupUnWin(self):
        pass
# --------------------------------------------------------------------------
    def bestPlace(self, listeCase):
        """
        On regarde la meilleurs case pour poser notre piece
        :return:
        """
        case = random.choice(listeCase)

        return case

# --------------------------------------------------------------------------
    def worstPiece(self, listePiece):
        """
        On donne a l'adversaire la piece avec le moins d'attribut en commun
        sur les places possibles
        :return:
        """
        piece = random.choice(listePiece)

        return piece
# --------------------------------------------------------------------------
    def piecesVoisine(self, case):
        pass
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

# ==============================================================================
# ==============================================================================
if __name__ == '__main__':
    tab = Tablier()
    pio = Pioche()
    j1 = Joueur('1')
    j2 = Joueur('2')
    t = Tour(j1, j2)
    ia = IA_random(tab, pio, t)
    print(ia.bestPlace())
    print(ia.worstPiece())
