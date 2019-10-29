from Piece import Piece
from Case import Case
from Tablier import Tablier

class Etat(object):

    def __init__(self, etatInitial: bool = False):
        self.etatInitial = etatInitial
        self.tablier = Tablier()

    @staticmethod
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

    # def isDiagoQuarto(self):
    #     if self.isQuarto(self.tablier['A1'], self.tablier['B2'], self.tablier['C3'], self.tablier['D4']):
    #         print("Quarto !! ")



etat1 = Etat(True) # a True la Partie commence et a False fin de la partie

idCase: str = 'A1'
idCase3: str = 'B2'
idCase4: str = 'C3'
idCase2: str = 'D4'


p1 = Piece("Marron", "Rond", "Grand", 1)
p2 = Piece("Beige", "Carré", "Petit", 1)
p3 = Piece("Beige", "Rond", "Grand", 1)
p4 = Piece("Marron", "Rond", "Petit", 1)
etat1.tablier.showTablier()
print("//////////////////////////////")

# etat1.tablier.poserPiece(idCase, p1)
# etat1.tablier.poserPiece(idCase2, p2)
# etat1.tablier.poserPiece(idCase3, p3)
# etat1.tablier.poserPiece(idCase4, p4)
# etat1.tablier.showTablier()
#
# etat1.isDiagoQuarto()
