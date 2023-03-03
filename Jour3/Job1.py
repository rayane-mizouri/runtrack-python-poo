class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouter_habitant(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        ville.ajouter_habitant()

    def ajouter_habitant(self):
        self.__ville.ajouter_habitant()

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville.get_nom()


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print("Nombre d'habitants de", paris.get_nom(), ":", paris.get_nombre_habitants())
print("Nombre d'habitants de", marseille.get_nom(), ":", marseille.get_nombre_habitants())

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


# Affichage du nombre d'habitants de Paris après l'ajout
print("Mise a jour de la ville de", paris.get_nom(), paris.get_nombre_habitants(), "habitants")
print("Mise a jour de la ville de", marseille.get_nom(), marseille.get_nombre_habitants(), "habitants")
