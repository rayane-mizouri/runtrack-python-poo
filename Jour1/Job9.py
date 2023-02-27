class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        self.calculer = self.prixHT * self.TVA

    def CalculerPrixTTC(self):
        return(self.calculer)

    def afficher(self):
        print("Le nom du produit est :",self.nom,f'\n',"Le prix du produit est :",self.prixHT,f'\n',"Le montant de la TVA est :",self.TVA,f'\n',"Le montant TTC est : ",self.calculer)

    def nom(self):
        return(self.nom)
    def prixHT(self):
        return(self.prixHT)
    def TVA(self):
        return(self.TVA)

Produit1 = Produit("Ordinateur",1260,1.2)
Produit1.afficher()
