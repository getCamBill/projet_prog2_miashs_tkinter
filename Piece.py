class Piece(object):

    def __init__(self, color: str, shape: str, size: str, dug: int):

        self.color: str = color
        self.shape: str = shape
        self.size: str = size
        self.dug: int = dug

    def getID(self):
        id :str = self.color[0] + self.shape[0] + self.size[0] + str(self.dug)
        return id


    def showCarac(self):
        print("Couleur : ", self.color, '\n'
              "Forme : ", self.shape, '\n'
              "Taille : ", self.size, '\n'
              "Creux : ", self.dug
              )


#p1 = Piece("Marron", "Rond", "Grand", 1)
#p1.showCarac()
#print("ID : " , p1.getID())