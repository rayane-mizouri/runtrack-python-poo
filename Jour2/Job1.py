class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def size(self):
        print("La longueur est :",self.__longueur,f'\n',"La largeur est :",self.__largeur)

Rectangle1 = Rectangle(10,5)
Rectangle1.size()

Rectangle2 = Rectangle(4,2)
Rectangle2.size()