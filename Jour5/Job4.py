liste = (10,23,45,123,3,89)
def nombre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        nombre_reste = nombre(liste[1:])
        return liste[0] if liste[0] > nombre_reste else nombre_reste


print(nombre(liste))