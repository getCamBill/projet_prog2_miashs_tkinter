class Piece(object):
    def __init__(self, color :str, shape :str, size :str, dug :bool):
        
        self.color :str = color
        self.shape :str = shape
        self.size :str = size
        self.dug :bool = dug

    def carac(self):
        print("Couleur : " ,self.color, \
              "Forme : " , self.shape, \
              "Taille : ", self.size, \
              "Creux : " , self.dug
              )

    def