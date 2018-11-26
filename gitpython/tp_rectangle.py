# -*- coding. utf-8 -*-
class Rectangle:
    #longueur=0
    #largeur=0
    def __init__(self,longueur=0,largeur=0):
        self._longueur=longueur
        self._largeur=largeur
        self._surface = largeur*longueur
    
    def get_largeur(self):
        return self.

    
r = Rectangle()
r1 = Rectangle(1,2)

print(r.largeur,r.longueur)
print(r1.largeur,r1.longueur)
print(r.surface)
print(r1.surface)