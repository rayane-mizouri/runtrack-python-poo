nombre = int(input("Veuillez entrer un nombre: "))

def factorielle(n):
    if n == 0:
        print(n)
        return 1
    else:
        print(n)
        return n  * factorielle(n-1)

factorielle(nombre)