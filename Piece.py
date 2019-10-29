class Piece(object):

    def __init__(self, color: str = None, shape: str = None, size: str = None, dug: int = None):

        self.color: str = color
        self.shape: str = shape
        self.size: str = size
        self.dug: int = dug

    def getID(self):
        id :str = self.color[0] + self.shape[0] + self.size[0] + str(self.dug)
        return id
    def getColor(self):
        return self.color

    def getShape(self):
        return self.shape

    def getDug(self):
        return self.dug

    def getSize(self):
        return self.size

    def showCarac(self):
        print("Couleur : ", self.color, '\n'
              "Forme : ", self.shape, '\n'
              "Taille : ", self.size, '\n'
              "Creux : ", self.dug
              )
