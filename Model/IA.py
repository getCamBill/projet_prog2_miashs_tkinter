"""
Classe IA:
Jouer contre l'ordi
"""
from Model.Tablier import Pioche, Tablier
from Model.Pioche import Piece
from Model.Tour import Tour
# ==============================================================================
class IA(object):

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
    def bestPlace(self):
        """
        On regarde la meilleurs case pour poser notre piece
        :return:
        """
        if self.tour == 0:
            # on met la piece en random
            pass
        else:
            # on cherhec les position avec des pieces avec le plus d'attre e commun
            pass

# --------------------------------------------------------------------------
    def worstPiece(self):
        """
        On donne a l'adversaire la piece avec le moins d'attribut en commun
        sur les places possibles
        :return:
        """
        pass
# --------------------------------------------------------------------------
    def piecesVoisine(self, case):

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

# ==============================================================================
# ==============================================================================
if __name__ == '__main__':
    tab = Tablier()
    pio = Pioche()
    ia = IA(tab, pio)
