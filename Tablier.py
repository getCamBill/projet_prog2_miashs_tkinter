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
                #piece = Piece()
                self.tablier[self.idPiece] = None


    def showTablier(self): # méthode pour débuguer
        for ele in self.tablier.values(): # ici la value qui ressort est un objet Case
            print("Id de la case : ",ele)

    #def isCaseValide(self, idCase: str):


    def poserPiece(self, idCase: str, piece: Piece):
        # renvoie la valeur du bool occuped donc si false alors place libre
        if self.tablier[idCase] == None:
            #self.tablier[idCase].occuped = True
            self.tablier[idCase] = piece
        else: # si la place est prise par une piece
            print("La position {0} est déjà occupée !".format(idCase))

    def isQuarto(self, p1: Piece, p2: Piece, p3: Piece, p4: Piece):
        """
        :type p1: Piece
        :argument p1: p1
        """

        NbAttrEnCommun: int = 0
        isAttrEnCommun: bool = False
        listAttrEnCommun: list = []

        if p1 and p2 and p3 and p4 != None:
            for val1 in p1.__dict__.values():
                for val2 in p2.__dict__.values():
                    for val3 in p3.__dict__.values():
                        for val4 in p4.__dict__.values():
                            if val1 == val2 and val2 == val3 and val3 == val4:
                                #print(val1, val2, val3, val4) # ligne pour débuguer
                                NbAttrEnCommun += 1
                                isAttrEnCommun = True
                                listAttrEnCommun.append(val4)

            return isAttrEnCommun #, NbAttrEnCommun, listAttrEnCommun



    def isDiagoQuarto(self): # renvoie True si Quarto,  None Sinon
        return self.isQuarto(self.tablier['A1'], self.tablier['B2'], self.tablier['C3'], self.tablier['D4']) \
                or self.isQuarto(self.tablier['A4'], self.tablier['B3'], self.tablier['C2'], self.tablier['D1'])
            #print("Quarto !! ")

    def isLigneQuarto(self): # renvoie True si Quarto,  None Sinon
        for i in ('1234'):
            return self.isQuarto(self.tablier['A'+i], self.tablier['B'+i], self.tablier['C'+i], self.tablier['D'+i])

    def isColonneQuarto(self): # renvoie True si Quarto,  None Sinon
        for lettre in ('ABCD'):
            return self.isQuarto(self.tablier[lettre+'1'], self.tablier[lettre+'2'], self.tablier[lettre+'3'], self.tablier[lettre+'4'])


idCase: str = 'A1'
idCase3: str = 'A2'
idCase4: str = 'C4'
idCase2: str = 'B3'

t1 = Tablier()
p1 = Piece("Marron", "Rond", "Grand", 1)
p2 = Piece("Beige", "Carré", "Petit", 1)
p3 = Piece("Beige", "Rond", "Grand", 1)
p4 = Piece("Marron", "Rond", "Petit", 1)


t1.poserPiece(idCase, p1)
t1.poserPiece(idCase2, p2)
t1.poserPiece(idCase3, p3)
t1.poserPiece(idCase4, p4)

#print(t1.isColonneQuarto())
#t1.isLigneQuarto()
#t1.isDiagoQuarto()
#t1.showTablier()