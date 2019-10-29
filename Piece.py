class Piece(object):

    def __init__(self, color: str, shape: str, size: str, dug: int):

        self.color: str = color
        self.shape: str = shape
        self.size: str = size
        self.dug: int = dug

    def getID(self):
        id :str = self.color[0] + self.shape[0] + self.size[0] + str(self.dug)
        return id
    def getColor(self):
        return self.color

    def getShape(self):
        return self.shape

    def getDug(self):
        return self.dug

    def getSize(self):
        return self.size

    def showCarac(self):
        print("Couleur : ", self.color, '\n'
              "Forme : ", self.shape, '\n'
              "Taille : ", self.size, '\n'
              "Creux : ", self.dug
              )



p1 = Piece("Marron", "Rond", "Grand", 1)
p2 = Piece("Beige", "Rond", "Petit", 0)
p3 = Piece("Beige", "Rond", "Grand", 1)
p4 = Piece("Marron", "Rond", "Petit", 1)

for val1 in p1.__dict__.values():
    for val2 in p2.__dict__.values():
        for val3 in p3.__dict__.values():
            for val4 in p4.__dict__.values():
                if val1 == val2 and val2 == val3 and val3 == val4:
                    print("Un attr en commun")
                else:
                    print("Nop")




# dict1 = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Name': 'Mahnaz', 'Age': 27}
# dict3 = {'Name': 'Abid', 'Age': 27}
# dict4 = {'Name': 'Zara', 'Age': 7}
#
#
# def cmp(a, b):
#     return (int(a) > int(b)) - (int(a) < int(b))
#
# val: int = len(dict1.values())
# val2: int = len(dict2.values())
#
# print("Val = ", val, '\n', "Val2 : ", val2)

