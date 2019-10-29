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
                #case = Case(self.idPiece)
                self.tablier[self.idPiece] = None


    def showTablier(self): # méthode pour débuguer
        for ele in self.tablier.items(): # ici la value qui ressort est un objet Case
            print("Id de la case : ",ele)


    def poserPiece(self, idCase: str, piece: Piece):
        # renvoie la valeur du bool occuped donc si false alors place libre
        if self.tablier[idCase] != None:
            #self.tablier[idCase].occuped = True
            self.tablier[idCase] = piece
        else: # si la place est prise par une piéce
            print("La position {0} est déjè occupée !".format(idCase))


idCase: str = 'A1'
idCase3: str = 'B2'
idCase4: str = 'C3'
idCase2: str = 'D4'

t1 = Tablier()
p1 = Piece("Marron", "Rond", "Grand", 1)
p2 = Piece("Beige", "Carré", "Petit", 1)
p3 = Piece("Beige", "Rond", "Grand", 1)
p4 = Piece("Marron", "Rond", "Petit", 1)
t1.showTablier()
print("//////////////////////////////")
t1.poserPiece(idCase, p1)
# t1.poserPiece(idCase2, p2)
# t1.poserPiece(idCase3, p3)
# t1.poserPiece(idCase4, p4)

t1.showTablier()

