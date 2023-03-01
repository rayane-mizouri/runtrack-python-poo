class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    def get_marque(self):
        return self._marque

    def set_marque(self, marque):
        self._marque = marque

    def get_modele(self):
        return self._modele

    def set_modele(self, modele):
        self._modele = modele

    def get_annee(self):
        return self._annee

    def set_annee(self, annee):
        self._annee = annee

    def get_kilometrage(self):
        return self._kilometrage

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    def is_en_marche(self):
        return self._en_marche

    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True

    def arreter(self):
        self._en_marche = False

    def _verifier_plein(self):
        return self._reservoir > 5


voiture1 = Voiture("BUGATTi", "MISTRAL", 2016, 10000)
voiture1.demarrer()
print(voiture1.is_en_marche())
voiture1.arreter()
print(voiture1.is_en_marche())
