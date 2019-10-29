from Piece import Piece
from Case import Case
from Tablier import Tablier

class Etat(object):

    def __init__(self, etatInitial: bool = False):
        self.etatInitial = etatInitial
        #Tablier().__init__()




# etat1 = Etat(True) # a True la Partie commence et a False fin de la partie
#
# idCase: str = 'A1'
# idCase3: str = 'B2'
# idCase4: str = 'C3'
# idCase2: str = 'D4'
#
#
# p1 = Piece("Marron", "Rond", "Grand", 1)
# p2 = Piece("Beige", "Carré", "Petit", 1)
# p3 = Piece("Beige", "Rond", "Grand", 1)
# p4 = Piece("Marron", "Rond", "Petit", 1)
# t1 = Tablier()
# t1.showTablier()
# print("//////////////////////////////")
# t1.poserPiece(idCase, p1)
# t1.poserPiece(idCase2, p2)
# t1.poserPiece(idCase3, p3)
# t1.poserPiece(idCase4, p4)
# t1.showTablier()
# print(t1.isQuarto(p1, p2, p3, p4))
# t1.isDiagoQuarto()