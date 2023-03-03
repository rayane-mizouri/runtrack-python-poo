class Tache:
    def __init__(self, titre, description, statut=False):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - {'Terminé' if self.statut else 'A faire'}"


class ListedeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = True

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


tache1 = Tache("Lire le sujet", "Finir le sujet.")
tache2 = Tache("git clone", "Créer un repo et le le clone")
tache3 = Tache("Rendre mon travail", "Git push")

liste = ListedeTaches()

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

liste.afficherListe()
liste.supprimerTache(tache1)
liste.marquerCommeFinie(tache2)
taches_a_faire = liste.filterListe(False)
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)