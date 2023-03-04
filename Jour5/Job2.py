nombre = int(input("Veuillez entrer un nombre: "))
puissance = int(input("Veuillez entrer une puissance"))

def factorielle(n,x):
    if n == 0:
        return 1
    temp = factorielle(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

resultat = factorielle(nombre, puissance)
print(f"{nombre}^{puissance} = {resultat}")