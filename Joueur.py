class Joueur(object):

    def __init__(self):
        self.jouer: bool = True
        self.pieceAttribuee: str = None

    def setPieceAttribuee(self, idPiece: str):
        self.pieceAttribuee = idPiece
