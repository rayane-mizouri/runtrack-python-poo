class Student:
    def __init__(self, prenom, nom, numero__etudiant, credits=0):
        self.__prenom = prenom
        self.__nom = nom
        self.__numero__etudiant = numero__etudiant
        self._credits = credits
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
        else:
            print("Invalid input: credits should be greater than 0.")

    def __studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        elif self._credits < 60:
            return "Insuffisant"

    def studentInfo(self):
        print("Prenom : ", self.__prenom)
        print("Nom : ", self.__nom)
        print("Identifiant etudiant : ", self.__numero__etudiant)
        print("Niveau : ", self.__studentEval())


Student1 = Student("John", "Doe", 145)
Student1.add_credits(11)
Student1.add_credits(10)
Student1.add_credits(9)

print("Le nombre de credits de John Doe est de ", Student1._credits,"points")

Student1 = Student("John", "Doe", 145)
Student1.add_credits(70)
Student1.studentInfo()