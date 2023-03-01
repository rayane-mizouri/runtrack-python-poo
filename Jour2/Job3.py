class Livre:
    def __init__(self, titre, auteur, nombre_de_page):
        self._titre = titre
        self._auteur = auteur
        self._nombre_de_page = nombre_de_page
        self._disponible = True

    def get_titre(self):
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nombre_de_page(self):
        return self._nombre_de_page

    def set_nombre_de_page(self, nombre_de_page):
        if isinstance(nombre_de_page, int) and nombre_de_page > 0:
            self._nombre_de_page = nombre_de_page
        else:
            print("Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self._disponible

    def emprunter(self):
        if self._disponible:
            self._disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Livre déjà emprunpté")

    def rendre(self):
        if not self._disponible:
            self._disponible = True
            print("Le livre a été rendu.")
        else:
            print("Vous n'avez pas de livre à rendre.")

    def afficher_livre(self):
        print(f'Titre : {self._titre}',f'\n',f'Auteur : {self._auteur}',f'\n',f'Nombre de pages : {self._nombre_de_page}',f'\n',f'Disponible : {self._disponible}')


Livre1 = Livre("mein kampf","Hitler",720)
Livre1.afficher_livre()
Livre1.set_nombre_de_page(720.20)
Livre1.emprunter()
Livre1.emprunter()
Livre1.rendre()
Livre1.rendre()
