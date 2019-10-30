from Pioche import Pioche
from Joueur import Joueur

class Tablier():

    def __init__(self):
        self.Pioche = Pioche().__init__()
        self.Joueur = Joueur().__init__()
        self.tablier = dict({}) # tablier de 16 cases avec id et valeur de la piece posée
        #-------------------------------
        self.i: int = 0
        for lettre in ("ABCD"):
            for val in ("1234"):
                self.tablier[lettre+val] = None

    def showTablier(self): # méthode pour débuguer
        for ele in self.tablier.items():
            if ele[1] == None: # si la case est dispo on l'affiche
                print(ele[0])

    def piecePourAdversaire(self, idPiece: str, joueur: Joueur):
        if self.isPieceValide(idPiece) != None:
            joueur.setPieceAttribuee(idPiece)
            return True
        else:
            print("La piece n'est pas au bon format. Ex: MRG1")

    def isCaseValide(self, idCase: str):
        # à modifier avec une recherche de valeur dans une liste à voir si plus rapide (méthode des LU)
            for lettre in ("ABCD"):
                for val in ("1234"):
                    if idCase == lettre + val:
                        return True

    def isPieceValide(self, idPiece: str):
        # à modifier avec une recherche de valeur dans une liste à voir si plus rapide (méthode des LU)
            for color in ("MB"):
                for shape in ("RC"):
                    for size in ("GP"):
                        for dug in ("10"):
                            if idPiece == color + shape + size + dug:
                                return True

    def poserPiece(self, joueur: Joueur, idCase: str, pioche: Pioche):

        if self.isCaseValide(idCase) != None:
            if pioche.__getitem__(joueur.pieceAttribuee):
                # si la piece est dans la pioche
                if self.tablier[idCase] == None:
                    # si la piece n'est pas None alors elle n'est pas encore posée
                    self.tablier[idCase] = joueur.pieceAttribuee
                    pioche.__setitem__(joueur.pieceAttribuee, None)
                    joueur.pieceAttribuee = None
                else:
                    print("La position {0} est déjà occupée !".format(idCase))
        else:
            print("La case n'est pas comprise entre A..D et 1..4")
    """
    Redéfinir la fonction pour les deux autres valeur de sorties
    """
    def isQuarto(self, idPiece1: str, idPiece2: str, idPiece3: str, idPiece4: str):
        #NbAttrEnCommun: int = 0
        isAttrEnCommun: bool = False
        #listAttrEnCommun: list = []

        if idPiece1 and idPiece2 and idPiece3 and idPiece4 != None:
            for attr1 in idPiece1:
                for attr2 in idPiece2:
                    for attr3 in idPiece3:
                        for attr4 in idPiece4:
                            if attr1 == attr2 and attr2 == attr3 and attr3 == attr4:
                                #NbAttrEnCommun += 1
                                isAttrEnCommun = True
                                #listAttrEnCommun.append(attr4)

            return isAttrEnCommun #, NbAttrEnCommun, listAttrEnCommun

    def isDiagoQuarto(self): # renvoie True si Quarto,  None Sinon
        return self.isQuarto(self.tablier['A1'], self.tablier['B2'], self.tablier['C3'], self.tablier['D4']) \
                or self.isQuarto(self.tablier['A4'], self.tablier['B3'], self.tablier['C2'], self.tablier['D1'])

    def isLigneQuarto(self): # renvoie True si Quarto,  False Sinon
        for i in ('1234'):
            if self.isQuarto(self.tablier['A'+i], self.tablier['B'+i], self.tablier['C'+i], self.tablier['D'+i]) == True:
                return True
        return False

    def isColonneQuarto(self): # renvoie True si Quarto,  False Sinon
        for lettre in ('ABCD'):
            if self.isQuarto(self.tablier[lettre+'1'], self.tablier[lettre+'2'], self.tablier[lettre+'3'], self.tablier[lettre+'4']) == True:
                return True
        return False