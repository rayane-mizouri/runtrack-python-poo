class Animal:
    def __init__(self,age,prenom):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age +=1
        print(self.age)

    def nommer(self):
        self.prenom = "Luna"
        print("L'animal se nomme ",self.prenom)

age = Animal(0,"")
age.vieillir()
age.nommer()