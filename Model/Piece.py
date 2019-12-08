class Piece(object):

    def __init__(self,color: str = None, shape: str = None, size: str = None, dug: int = None):

        self.color: str = color
        self.shape: str = shape
        self.size: str = size
        self.dug: int = dug

    def showCarac(self):
        return self.color, self.shape, self.size, self.dug