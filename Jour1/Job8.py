class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
        self.cironference = self.rayon * 3,14
        self.aire = self.rayon * self.rayon * 3.14
        self.diametre = self.rayon * 2

    def changerRayon(self):
        pass

    def afficherInfos(self):
        print("Le rayon est : ",self.rayon, f'\n',"La cironférence est : ",self.cironference,f'\n',"L'aire du carré est : ",self.aire,f'\n',"le diamètre est : ", self.diametre)

    def circonference(self):
        return(self.cironference)

    def aire(self):
        return(self.aire)

    def diametre(self):
        return(self.diametre)

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle2 = Cercle(7)
cercle2.afficherInfos()