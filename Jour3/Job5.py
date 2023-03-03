class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 1


class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        while True:
            niveau = input("Choisissez un niveau de difficulté (1, 2 ou 3) : ")
            if niveau in ("1", "2", "3"):
                self.niveau = int(niveau)
                break
            else:
                print("Niveau invalide. Veuillez choisir un niveau entre 1 ,2 ou 3.")

    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 100
            vie_ennemi = 100
        else:
            vie_joueur = 50
            vie_ennemi = 100

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while True:
            print(f'{joueur.nom} ({joueur.vie} PV) affronte {ennemi.nom} ({ennemi.vie} PV)')
            joueur.attaquer(ennemi)
            self.verifierSante(ennemi)
            if ennemi.vie <= 0:
                print(f'{joueur.nom} a vaincu {ennemi.nom} !')
                self.verifierGagnant(joueur, ennemi)
                break
            ennemi.attaquer(joueur)
            self.verifierSante(joueur)
            if joueur.vie <= 0:
                print(f'{ennemi.nom} a vaincu {joueur.nom} !')
                self.verifierGagnant(joueur, ennemi)
                break

    def verifierSante(self, personnage):
        if personnage.vie <= 0:
            print(f'{personnage.nom} est K.O. !')

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie > ennemi.vie:
            print(f'{joueur.nom} a win gg !')
        elif ennemi.vie > joueur.vie:
            print(f'{ennemi.nom} a gagné tu es claqué mdr!')
        elif joueur.vie == ennemi:
            print("Match nul bien joué!")


Jeu1 = Jeu()
Jeu1.lancerJeu()
