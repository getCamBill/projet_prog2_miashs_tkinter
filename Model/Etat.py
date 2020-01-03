from Model.Tablier import *
class Etat(object):

    def __init__(self, Tablier: Tablier = None):
        """
        On initialis l'état du jeu avec en paramètre le tablier de Jeu
        :param Tablier:
        """
        self.victoire = False
        self.egalite = False
        self.Tablier = Tablier
    def vict(self):
        """
        Au bout de 3 tour le programme vérifie si il y a une situationde Quarto
        :return:
        """
        # on appelle les fonctions seulement au bout de 3 tours
        if self.Tablier.isDiagoQuarto() or \
                self.Tablier.isLigneQuarto() or \
                self.Tablier.isColonneQuarto():
            self.victoire = True
            return "QUARTO !!"
        else:
            return ''