from Piece import Piece
from Tablier import Tablier

class Etat(object):

    def __init__(self, etatInitial: bool = False):
        self.etatInitial = etatInitial
        self.victoire = False
        self.egalite = False

