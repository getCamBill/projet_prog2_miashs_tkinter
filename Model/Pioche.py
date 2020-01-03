from Model.Piece import Piece

class Pioche(object):

    def __init__(self):
        """

        """
        self.Pioche = dict({})
        for color in ("M", "B"):
            for shape in ("R", "C"):
                for size in ("G", "P"):
                    for dug in (1, 0):
                        self.idPiece: str = color + shape + size + str(dug)
                        piece: Piece = Piece(color, shape, size, dug)
                        self.Pioche[self.idPiece] = piece

    def showPieces(self):
        """
        Méthode pour le quarto non graphique
        :return:
        """
        print("Pièces disponibles : ")
        [print("Id : ",ele) for ele in self.Pioche.keys()]

    def listPieceDispo(self):
        """

        :return:
        """
        return [ele for ele in self.Pioche.keys()]
    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        try:
            return self.Pioche[item]
        except:
            print("La pièce est déjà posée ! ")

    def __setitem__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        del self.Pioche[key]

# if __name__ == "__main__":
#     p1 = Pioche()
#     p1.showPieces()
#     # print(p1.Pioche['MRG1'].showCarac())
#     print(p1.Pioche.items())
#     print(p1.Pioche.get('MRG1'))