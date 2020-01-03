from Model import Pioche, Joueur


class Tablier():

    def __init__(self):
        """

        """
        self.tablier = dict({})  # tablier de 16 cases avec id et valeur de la piece posée as an object
        # -------------------------------
        # self.i: int = 0
        for lettre in ("ABCD"):
            for val in ("1234"):
                self.tablier[lettre + val] = None

    def piecePourAdversaire(self, idPiece: str, joueur: Joueur):
        """

        :param idPiece:
        :param joueur:
        :return:
        """
        if self.isPieceValide(idPiece) != None:
            joueur.setPieceAttribuee(idPiece)
            return True
        else:
            print("La piece n'est pas au bon format. Ex: MRG1")

    def isCaseValide(self, idCase: str):
        """

        :param idCase:
        :return:
        """
        # à modifier avec une recherche de valeur dans une liste à voir si plus rapide (méthode des LU)
        for lettre in ("ABCD"):
            for val in ("1234"):
                if idCase == lettre + val:
                    return True

    def isPieceValide(self, idPiece: str):
        """

        :param idPiece:
        :return:
        """
        # à modifier avec une recherche de valeur dans une liste à voir si plus rapide (méthode des LU)
        for color in ("MB"):
            for shape in ("RC"):
                for size in ("GP"):
                    for dug in ("10"):
                        if idPiece == color + shape + size + dug:
                            return True

    def poserPiece(self, joueur: Joueur, idCase: str, pioche: Pioche):
        """

        :param joueur:
        :param idCase:
        :param pioche:
        :return:
        """

        if self.isCaseValide(idCase) != None:
            if pioche.__getitem__(joueur.pieceAttribuee):
                # si la piece est dans la pioche
                if self.tablier[idCase] == None:
                    # si la piece n'est pas None alors elle n'est pas encore posée
                    self.tablier[idCase] = joueur.pieceAttribuee  # la case prend les attributes de la piece
                    pioche.__setitem__(joueur.pieceAttribuee, None)  # on retire la piece de la pioche en la supp
                    joueur.pieceAttribuee = None
                else:
                    print("La position {0} est déjà occupée !".format(idCase))
                    return 1
            else:
                return 1
        else:
            print("La case n'est pas au bon format")

    def isAttrEnCommun(self, idPiece1: str, idPiece2: str, idPiece3: str, idPiece4: str):
        """

        :param idPiece1:
        :param idPiece2:
        :param idPiece3:
        :param idPiece4:
        :return:
        """
        # NbAttrEnCommun: int = 0
        isAttrEnCommun: bool = False
        # listAttrEnCommun: list = []

        if idPiece1 and idPiece2 and idPiece3 and idPiece4:
            for attr1 in idPiece1:
                for attr2 in idPiece2:
                    for attr3 in idPiece3:
                        for attr4 in idPiece4:
                            if attr1 == attr2 and attr2 == attr3 and attr3 == attr4:
                                # NbAttrEnCommun += 1
                                isAttrEnCommun = True
                                # listAttrEnCommun.append(attr4)

            return isAttrEnCommun  # , NbAttrEnCommun, listAttrEnCommun

    def isDiagoQuarto(self):  # renvoie True si Quarto,  None Sinon
        """

        :return:
        """
        return self.isAttrEnCommun(self.tablier['A1'], self.tablier['B2'], self.tablier['C3'], self.tablier['D4']) \
               or self.isAttrEnCommun(self.tablier['A4'], self.tablier['B3'], self.tablier['C2'], self.tablier['D1'])

    def isLigneQuarto(self):  # renvoie True si Quarto,  False Sinon
        """

        :return:
        """
        for i in ('1234'):
            if self.isAttrEnCommun(self.tablier['A' + i], self.tablier['B' + i], self.tablier['C' + i],
                                   self.tablier['D' + i]) == True:  # virer le == True
                return True
        return False

    def isColonneQuarto(self):  # renvoie True si Quarto,  False Sinon
        """

        :return:
        """
        for lettre in ('ABCD'):
            if self.isAttrEnCommun(self.tablier[lettre + '1'], self.tablier[lettre + '2'], self.tablier[lettre + '3'],
                                   self.tablier[lettre + '4']) == True:  # virer le == True
                return True
        return False

    def isCarreQuarto(self):  # méthode à dev pour un level sup du jeux
        """

        :return:
        """
        return self.isAttrEnCommun(self.tablier['A1'], self.tablier['A2'], self.tablier['B1'], self.tablier['B2']) \
               or self.isAttrEnCommun(self.tablier['B1'], self.tablier['B2'], self.tablier['C1'], self.tablier['C2']) \
               or self.isAttrEnCommun(self.tablier['C1'], self.tablier['C2'], self.tablier['D1'], self.tablier['D2']) \
               or self.isAttrEnCommun(self.tablier['A2'], self.tablier['A3'], self.tablier['B2'], self.tablier['B3']) \
               or self.isAttrEnCommun(self.tablier['B2'], self.tablier['B3'], self.tablier['C2'], self.tablier['C3']) \
               or self.isAttrEnCommun(self.tablier['C2'], self.tablier['C3'], self.tablier['D2'], self.tablier['D3']) \
               or self.isAttrEnCommun(self.tablier['A3'], self.tablier['A4'], self.tablier['B3'], self.tablier['B4']) \
               or self.isAttrEnCommun(self.tablier['B3'], self.tablier['B4'], self.tablier['C3'], self.tablier['C4']) \
               or self.isAttrEnCommun(self.tablier['C3'], self.tablier['C4'], self.tablier['D3'], self.tablier['D4'])

    def isQuarto(self, level):
        """
        En fonction du niveau choisi on vérifie different quarto possible
        :param level:
        :return:
        """
        if level == 1:
            if self.isLigneQuarto() or self.isColonneQuarto():
                return True
        elif level == 2:
            if self.isDiagoQuarto() or self.isLigneQuarto() or self.isColonneQuarto():
                return True
        elif level == 3:
            if self.isDiagoQuarto() or \
                    self.isLigneQuarto() or \
                    self.isColonneQuarto() or \
                    self.isCarreQuarto():
                return True
