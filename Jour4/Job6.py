class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.model)
        print("Année :", self.annee)
        print("Prix :", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix, portes=4):
        super().__init__(marque, model, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        print("La voiture démarre !")


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix, roue=2):
        super().__init__(marque, model, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)

    def demarrer(self):
        print("La moto démarre !")


voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture1.informationsVehicule()
voiture1.demarrer()

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()