# def isQuarto(self, p1: Piece, p2: Piece, p3: Piece, p4: Piece):
    #     """
    #     :type p1: Piece
    #     :argument p1: p1
    #     """
    #
    #     NbAttrEnCommun: int = 0
    #     isAttrEnCommun: bool = False
    #     listAttrEnCommun: list = []
    #
    #     if p1 and p2 and p3 and p4 != None:
    #         for val1 in p1.__dict__.values():
    #             for val2 in p2.__dict__.values():
    #                 for val3 in p3.__dict__.values():
    #                     for val4 in p4.__dict__.values():
    #                         if val1 == val2 and val2 == val3 and val3 == val4:
    #                             #print(val1, val2, val3, val4) # ligne pour débuguer
    #                             NbAttrEnCommun += 1
    #                             isAttrEnCommun = True
    #                             listAttrEnCommun.append(val4)
    #
    #         return isAttrEnCommun #, NbAttrEnCommun, listAttrEnCommun

#///////////////////////////////////////////////////////////////////////////

# def poserPiece(self, idCase: str, idPiece: str, pioche: Pioche):
    #
    #     if self.isCaseValide(idCase) != None:
    #         if self.isPieceValide(idPiece) != None:
    #             if pioche.__getitem__(idPiece):
    #                 # si pas d'objet piece alors on met u piece
    #                 if self.tablier[idCase] == None:
    #                     # si la piece n'est pas None alors elle n'est pas encore posée
    #                     self.tablier[idCase] = idPiece
    #                     pioche.__setitem__(idPiece, None)
    #                 else:
    #                     print("La position {0} est déjà occupée !".format(idCase))
    #         else:
    #             print("La piece n'est pas au bon format ex: MRG1")
    #     else:
    #         print("La case n'est pas comprise entre A..D et 1..4")