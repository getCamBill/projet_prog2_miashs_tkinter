class Joueur(object):

    def __init__(self):
        self.jouer: bool = False
        self.distrib: bool = False
        self.pieceAttribuee: str = ""

    def setPieceAttribuee(self, idPiece: str):
        self.pieceAttribuee = idPiece


