class Rectangle:
    def __init__(self, longueur=0, largeur=0):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        perimetre = self.get_longueur() + self.get_largeur() * 2
        print("Le perimètre est de :", perimetre)

    def surface(self):
        surface = self.get_longueur() * self.get_largeur()
        print("la surface est de :", surface)

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur=0, largeur=0, hauteur=0):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        volume = self.get_longueur() * self.get_largeur() * self.__hauteur
        print("le volume est de :", volume)

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


rectangle1 = Rectangle(10, 5)
rectangle1.surface()
rectangle1.perimetre()

parallelepipede1 = Parallelepipede(10, 5, 2)
parallelepipede1.volume()
