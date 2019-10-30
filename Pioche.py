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
        for ele in self.Pioche.items():
            print(ele)

    def __getitem__(self, item):
        try:
            return self.Pioche[item]
        except:
            print("La pièce est déjà posée ! ")

    def __setitem__(self, key, value):
        del self.Pioche[key]


# p1 = Pioche()
# #p1.showPieces()
# piece = Piece()
# print(p1['MRG0'])
# print("Pièce vide",piece)
# piece = p1.__getitem__('MRG0')
# print(p1.__getitem__('MRG0'))
# p1.__setitem__('MRG0', None)
# #p1.showPieces()
# print("Piece vide est devenu : ",piece)






# listePieces = [
#     Piece("Marron", "Rond", "Grand", 1),
#     Piece("Marron", "Rond", "Grand", 0),
#     Piece("Marron", "Rond", "Grand", 1),
#     Piece("Marron", "Rond", "Grand", 0),
#     Piece("Marron", "Carré", "Petit", 1),
#     Piece("Marron", "Carré", "Petit", 0),
#     Piece("Marron", "Carré", "Petit", 1),
#     Piece("Marron", "Carré", "Petit", 0),
#     Piece("Beige", "Carré", "Petit", 1),
#     Piece("Beige", "Carré", "Petit", 0),
#     Piece("Beige", "Carré", "Petit", 1),
#     Piece("Beige", "Carré", "Petit", 0),
#     Piece("Beige", "Rond", "Grand", 1),
#     Piece("Beige", "Rond", "Grand", 0),
#     Piece("Beige", "Rond", "Grand", 1),
#     Piece("Beige", "Rond", "Grand", 0)
# ]
