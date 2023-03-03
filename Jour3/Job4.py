class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"{self.nom} ({self.position}, n°{self.numero}) :")
        print(f" - Buts : {self.buts}")
        print(f" - Passes décisives : {self.passes}")
        print(f" - Cartons jaunes : {self.cartons_jaunes}")
        print(f" - Cartons rouges : {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action invalide")
                return
        print(f"Joueur {nom_joueur} non trouvé dans l'équipe {self.nom}")



joueur1 = Joueur("Kylian Mbappé", 7, "attaquant")
joueur2 = Joueur("Hugo Lloris", 1, "gardien")
joueur3 = Joueur("Benjamin Pavard", 2, "défenseur")
equipe1 = Equipe("numéro 1")
equipe2 = Equipe("numéro 2")
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur1)
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
equipe2.mettreAJourStatistiquesJoueur("Kylian Mbappé", "but")
equipe1.mettreAJourStatistiquesJoueur("Benjamin Pavard", "carton jaune")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()