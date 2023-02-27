class Personne:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def affichername(self):
        print("Je suis " + self.prenom + " "+ self.nom)

personne1 = Personne("Doe","John")
personne1.affichername()

personne2 = Personne("Dupond","Jean")
personne2.affichername()

