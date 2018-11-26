class Rectangle:

    # longueur = 0
    # largeur = 0

    def __init__(self,longueur=0,largeur=0):
        self._longueur = longueur
        self._largeur = largeur
        print('def __init__(self,longueur=0,largeur=0)')

    def get_largeur(self):
        return self._largeur
    def set_largeur(self,largeur):
            self._largeur = largeur

    def get_longueur(self):
        return self._longueur
    def set_longueur(self,longueur):
            self._longueur = longueur

    def calcSurface(self):
        return self._longueur*self._largeur

class Carre(Rectangle):
    def __init__(self,cote=0):
        super().__init__(cote,cote)
        self.cote=cote
        print('def__init__(self,cote)')

#r = Rectangle()
#r1 = Rectangle(1,2)

#print(r.get_largeur())
c = Carre(2)
print('c')
