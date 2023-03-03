class CompteBancaire:
    def __init__(self, numero_de_compte, nom, prenom, solde, decouvert = False):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print("Votre numéro de compte est :", self.__numero_de_compte)
        print("Votre nom est :", self.__nom)
        print("Votre prénom est :", self.__prenom)
        print("Votre solde est de :", self.__solde)

    def afficherSolde(self):
        print(self.__solde)

    def versement(self, montant):
        self.__solde = self.__solde + montant
        print("Le versement de", montant, "a été effectué. Nouveau solde :", self.__solde)

    def retrait(self, montant):
        if self.decouvert or self.__solde >= montant:
            self.__solde = self.__solde - montant
            print("Le retrait de", montant, "a été effectué. Nouveau solde :", self.__solde)
        else:
            print("Solde insuffisant.")

    def agios(self, taux):
        if self.__solde < 0:
            montant_agios = -self.__solde * taux
            self.__solde = self.__solde - montant_agios
            print("Des agios ont été appliqués. Nouveau solde :", self.__solde)

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde = self.__solde - montant
            compte_destinataire.versement(montant)
            print("Le virement de", montant, "a été effectué vers le compte", compte_destinataire.__numero_de_compte)
        else:
            print("Solde insuffisant pour effectuer le virement.")


CompteBancaire1 = CompteBancaire(123,"Nom","Prénom",10000)
CompteBancaire1.afficher()
CompteBancaire1.afficherSolde()
CompteBancaire1.versement(999)
CompteBancaire1.retrait(9)

CompteBancaire2 = CompteBancaire(1234, "Nom2", "Prénom2", -5000, decouvert=True)
CompteBancaire2.afficher()
CompteBancaire2.virement(CompteBancaire1, 10000)



