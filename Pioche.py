from Piece import Piece
# La Pioche est un objet qui contient une liste d'objet 'Piece'

class Pioche(object):

    def __init__(self):
        self.i: int = 0
        self.Pioche = dict({})
        for color in ("Marron", "Beige"):
            for shape in ("Rond", "Carré"):
                for size in ("Grand", "Petit"):
                    for dug in (1, 0):
                        self.idPiece: str = color[0] + shape[0] + size[0] + str(dug)
                        piece: Piece = Piece(color, shape, size, dug)
                        self.Pioche[self.idPiece] = piece
                        self.i += 1

    def showPieces(self):
        print("Pièces disponibles : ")
        for ele in self.Pioche.keys():
            print("Id : ",ele)

    def __getitem__(self, item):
        try:
            return self.Pioche[item]
        except:
            print("La pièce est déjà posée ! ")

    def __setitem__(self, key, value):
        del self.Pioche[key]