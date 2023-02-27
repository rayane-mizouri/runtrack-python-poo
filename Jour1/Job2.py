class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def numbers(self):
        print("Le nombre1 est " , self.nombre1 ,f'\n'" le nombre2 est ",self.nombre2)

Operation2 = Operation(12, 3)
Operation2.numbers()