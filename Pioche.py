from Piece import Piece
# La Pioche est un objet qui contient une liste d'objet 'Piece'

class Pioche(object):

    def __init__(self):
        self.i: int = 0

        self.Pioche = []
        for color in ("Marron", "Beige"):
            for shape in ("Rond", "Carré"):
                for size in ("Grand", "Petit"):
                    for dug in (1, 0):
                        piece: Piece = Piece(color, shape, size, dug)
                        self.Pioche.append(piece)
                        self.i += 1

    def showPiece(self):
        for pce in self.Pioche:
            print(pce.getID())



p1 = Pioche()
#p1.showPiece()
