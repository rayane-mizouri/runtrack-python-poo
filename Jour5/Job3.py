def chaine_caractère(chaine):
    if chaine == "":
        print(chaine)
        return 0
    else:
        print(chaine)
        return 1 + chaine_caractère(chaine[1:])


liste = input("Veuillez rentrer des caractères: ")

chaine_caractère(liste)