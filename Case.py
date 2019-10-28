from Piece import Piece

class Case(object):

    def __init__(self, id: str):
        self.id: str = id
        self.attributs: Piece = None
        self.liens: list = []
        self.occuped: bool = False

    def pieceAttrToCase(self, pieceAttr: Piece):
    # méthode à revoir avec une boucle ou autre itérations pour chaque val
        self.couleur: str = pieceAttr.getColor()
        self.shape: str = pieceAttr.getShape()
        self.size: str = pieceAttr.getSize()
        self.dug: int = pieceAttr.getDug()

    #def getCaseVoisines(self):
