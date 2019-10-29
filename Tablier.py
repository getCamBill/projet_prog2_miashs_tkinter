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
                self.idPiece = lettre+val
                case = Case(self.idPiece)
                self.tablier[self.idPiece] = case


    def showTablier(self):
        for ele in self.tablier.values(): # ici la value qui ressort est un objet Case
            print("Id de la case : ",ele.showId(),
                  " Occupée : ",ele.occuped)


    def poserPiece(self, idCase: str, piece: Piece):
        # renvoie la valeur du bool occuped donc si false alors place libr
        if not self.tablier[idCase].isCaseLibre():
            self.tablier[idCase].occuped = True
            self.tablier[idCase].pieceAttrToCase(piece)
        else: # si la place est prise par une piéce
            print("La position {0} est déjè occupée !".format(idCase))


idCase: str = 'A2'
idCase2: str = 'D4'
t1 = Tablier()
p1 = Piece("Marron", "Rond", "Grand", 1)
p2 = Piece("Beige", "Rond", "Petit", 1)
t1.showTablier()
print("//////////////////////////////")
t1.poserPiece(idCase, p1)
t1.poserPiece(idCase2, p2)
t1.showTablier()
t1.poserPiece(idCase, p1)
t1.poserPiece(idCase2, p2)
