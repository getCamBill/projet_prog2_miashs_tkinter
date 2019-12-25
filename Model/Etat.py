from Model.Tablier import *
class Etat(object):

    def __init__(self, Tablier: Tablier = None):
        """

        :param Tablier:
        """
        self.victoire = False
        self.egalite = False
        self.Tablier = Tablier
    def vict(self):
        """

        :return:
        """
        # on appelle les fonctions seulement au bout de 4 tours
        if self.Tablier.isDiagoQuarto() or \
                self.Tablier.isLigneQuarto() or \
                self.Tablier.isColonneQuarto():
            self.victoire = True
            return "QUARTO !!"
        else:
            return ''