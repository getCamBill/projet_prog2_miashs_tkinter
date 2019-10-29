from Pioche import Pioche
from Piece import Piece
from Case import Case

class Tablier(object):

    def __init__(self):

        self.tablier = dict({}) # tablier de 16 cases avec id et valeur de la piece posée
        #-------------------------------
        self.i: int = 0
        for lettre in ("ABCD"):
            for val in ("1234"):
                self.i += 1
                self.id = lettre+val
                case = Case(self.idPiece)
                self.tablier[self.i] = {self.id: case}

    def showTablier(self):
        print(self.tablier.values())

    #def isCaseLibre(self, case: str): # case est définie par 'B2' par ex


    def poserPiece(self, case: str, pieceID: str):


t1 = Tablier()
t1.showTablier()