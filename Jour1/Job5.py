class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherLespoints(self):
        print("Je suis ",self.x,self.y)

afficheXY = Point(10,11)
afficheXY.afficherLespoints()

changeXY = Point(12,13)
changeXY.afficherLespoints()


