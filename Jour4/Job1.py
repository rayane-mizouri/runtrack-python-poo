class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def afficherMatiere(self):
        print("La matière enseignée est :", self.__matiereEnseignee)

Personne1 = Personne()
Personne1.afficherAge()
Personne1.bonjour()
Personne1.modifierAge(18)
Personne1.afficherAge()

Eleve1 = Eleve()
Eleve1.allerEnCours()
Eleve1.affichageAge()
Eleve1.modifierAge(21)
Eleve1.affichageAge()

Professeur1 = Professeur("Informatique")
Professeur1.afficherMatiere()
Professeur1.enseigner()
Professeur1.modifierAge(28)
Professeur1.afficherAge()
