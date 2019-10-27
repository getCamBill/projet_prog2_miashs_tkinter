from Piece import Piece

class Pioche(object):

    def __init__(self):
        i: int = 0
        self.pioche = dict({})
        for color in ("Marron", "Beige"):
            for shape in ("Rond", "Carré"):
                for size in ("Grand", "Petit"):
                    for dug in (1, 0):
                        piece = Piece(color, shape, size, dug)
                        self.pioche[i] = {i: piece}
                        i += 1

    def showPiece(self):
        self.pioche



p1 = Pioche()
print(p1.get)
