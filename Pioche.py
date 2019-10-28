from Piece import Piece

class Pioche(object):

    def __init__(self):
        i: int = 0
        #self.pioche = dict({}) # la pioche de piece est une liste d'objet
        self.pioche = []
        for color in ("Marron", "Beige"):
            for shape in ("Rond", "Carré"):
                for size in ("Grand", "Petit"):
                    for dug in (1, 0):
                        piece: Piece = Piece(color, shape, size, dug)
                        self.pioche.append(piece)
                        i += 1

    def showPiece(self):
        for pce in self.pioche:
            print(pce.getID())



p1 = Pioche()
#p1.showPiece()
