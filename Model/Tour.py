from Model.Joueur import *

class Tour(object):

    def __init__(self, joueur1, joueur2):
        self.tour: int = 0
        self.J1 = joueur1
        self.J2 = joueur2

    def auTourDe(self):
        if self.tour % 2 == 0:  # un tour sur deux un joueur peux jouer
            return (self.J2, self.J1)
        else:
            return (self.J1, self.J2)
