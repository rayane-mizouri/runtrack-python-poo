class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, nom, prix):
        self.__plats[nom] = {"prix": prix, "statut": "en cours"}

    def annuler_commande(self):
        self.__statut = "annulée"
        for plat in self.__plats:
            self.__plats[plat]["statut"] = "annulé"

    def __total(self):
        total = 0
        for plat in self.__plats:
            if self.__plats[plat]["statut"] != "annulé":
                total += self.__plats[plat]["prix"]
        return total

    def afficher_commande(self):
        print("Numéro de commande :", self.__num_commande)
        print("Liste des plats commandés :")
        for plat in self.__plats:
            print("- {} ({} €)".format(plat, self.__plats[plat]["prix"]))
        print("Total à payer : {} €".format(self.__total()))

    def calculer_tva(self, taux):
        prix_ttc = self.__total() * (1 + taux / 100)
        return round(prix_ttc - self.__total(), 2)

Commande1 = Commande("n°1")
Commande1.ajouter_plat("pokeball", 12.50)
Commande1.afficher_commande()
tva = Commande1.calculer_tva(20)
print("TVA à payer : {} €".format(tva))
Commande1.annuler_commande()
Commande1.afficher_commande()
