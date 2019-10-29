from Piece import Piece
from Tablier import Tablier

class Etat(object):

    def __init__(self, etatInitial: bool = False):
        self.etatInitial = etatInitial

    def isQuarto(self, p1: Piece, p2: Piece, p3: Piece, p4: Piece):
        """
        :type p1: Piece
        :argument p1: p1
        """
        NbAttrEnCommun: int = 0
        isAttrEnCommun: bool = False
        listAttrEnCommun: list = []

        for val1 in p1.__dict__.values():
            for val2 in p2.__dict__.values():
                for val3 in p3.__dict__.values():
                    for val4 in p4.__dict__.values():
                        if val1 == val2 and val2 == val3 and val3 == val4:
                            #print(val1, val2, val3, val4) # ligne pour débuguer

                            NbAttrEnCommun += 1
                            isAttrEnCommun = True
                            listAttrEnCommun.append(val4)

        return isAttrEnCommun #, NbAttrEnCommun, listAttrEnCommun

    # def isLigneQuarto(self, p1: Piece, p2: Piece, p3: Piece, p4: Piece):
    # def isColonneQuarto(self, p1: Piece, p2: Piece, p3: Piece, p4: Piece):
    # def isDiagoQuarto(self, p1: Piece, p2: Piece, p3: Piece, p4: Piece):



etat1 = Etat(True) # a True la Partie commence et a False fin de la partie

p1 = Piece("Marron", "Rond", "Grand", 1)
p2 = Piece("Beige", "Rond", "Petit", 1)
p3 = Piece("Beige", "Rond", "Grand", 1)
p4 = Piece("Marron", "Rond", "Petit", 1)

# p1 = Piece("Marron", "Rond", "Grand", 1)
# p2 = Piece("Beige", "Carré", "Petit", 1)
# p3 = Piece("Beige", "Rond", "Grand", 0)
# p4 = Piece("Marron", "Rond", "Petit", 1)

print(etat1.isQuarto(p1, p2, p3, p4))
