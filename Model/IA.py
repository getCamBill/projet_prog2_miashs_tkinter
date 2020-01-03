"""
Classe IA:
Jouer contre l'ordi
"""

from Model.Tablier import Tablier
from Model.Pioche import Pioche
from Model.Tour import Tour
from Model.Joueur import Joueur
import random
# ==============================================================================
class IA_random(object):

    def __init__(self, TablierParam: Tablier = None, Pioche: Pioche = None, Tour: Tour = None):
        self.tablier = TablierParam
        self.pieces = Pioche
        self.tour = Tour.tour
        self.mirror = Tablier()
        # self.tablierMiroir()
        print(self.mirror.tablier.keys())
# --------------------------------------------------------------------------

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
        # for placeDispo in list(listeCase.items()):
        #     self.mirror.tablier[placeDispo[0]] = placeDispo[1]
        #     if self.mirror.isQuarto():
        #         # self.mirror.tablier[placeDispo[0]] = placeDispo[1]
        #         idcase = placeDispo[0]
        #         btn  = placeDispo[1]
        #         return (idcase, btn)
        #     else:
        #         del self.mirror.tablier[placeDispo[0]]

        idcase, btn = random.choice(list(listeCase.items()))
        return (idcase, btn)

# --------------------------------------------------------------------------
    def worstPiece(self, listePiece):
        """
        On donne a l'adversaire la piece avec le moins d'attribut en commun
        sur les places possibles
        :return:
        """
        # print(listePiece.items())
        idpce, btn = random.choice(list(listePiece.items()))

        # print((idpce, btn))
        return (idpce, btn)

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
