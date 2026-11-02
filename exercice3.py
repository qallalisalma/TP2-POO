class Livre:
    def __init__(self, titre="Sans titre", auteur="Inconnu", annee=2026):      

     self.titre = titre
     self.auteur = auteur
     self.annee = annee
     self.disponible = True

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def afficher(self):
        if self.disponible:
            etat = "disponible" 
        else:
            etat = "indisponible"
        print(f"{self.titre} - {self.auteur} ({self.annee}) - {etat}")

l1 = Livre("La Boite a merveilles", "Sefrioui", 1954) 
l4 = Livre()

l1.afficher()
l4.afficher()
