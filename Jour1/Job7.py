class Personnage:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x = -1
        self.y = 0

    def droite(self):
        self.x = 1
        self.y = 0

    def bas(self):
        self.x = 0
        self.y = -1

    def haut(self):
        self.x = 0
        self.y = 1

    def position(self):
        return(self.x , self.y)

Personnage1 = Personnage(0,0)
print(Personnage1.position())
Personnage1.gauche()
print(Personnage1.position())
Personnage1.droite()
print(Personnage1.position())
Personnage1.bas()
print(Personnage1.position())
Personnage1.haut()
print(Personnage1.position())