from Controller.BDD import *


class Joueur(object):

    def __init__(self, pseudo: str = ""):
        """

        :param pseudo:
        """

        self.pseudo: str = pseudo
        self.jouer: bool = False

        self.database: str = 'C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db'
        self.conn = create_connection(self.database)

        if not select_joueur(self.conn, self.pseudo):
            create_joueur(self.conn, (self.pseudo, 0, 0))

    def setPieceAttribuee(self, idPiece: str):
        """

        :param idPiece:
        :return:
        """
        self.pieceAttribuee = idPiece

    def setInfoJoueur(self, win: int, lose: int):
        """

        :param win:
        :param lose:
        :return:
        """
        with self.conn:
            update_partie_joueur(self.conn, (win, lose, self.pseudo))

    def show(self):
        """

        :return:
        """
        with self.conn:
            print("1. Classement des joueurs par victoire:")
            select_joueur_by_victory(self.conn)
