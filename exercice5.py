class Livre:
    def __init__(self,titre,auteur,annee): 
        if titre == "":
            raise ValueError("le titre est vide")
        if annee < 1450 or annee > 2026:
            raise ValueError(f"annee impossible : {annee}")      

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
l1.afficher()

try:
    l2 = Livre("Le Passe simple", "Chraibi", 3054)
    l2.afficher()
except ValueError as e:
    print("Livre refuse :", e)

try:
    l3 = Livre("", "Anonyme", 2000)
    l3.afficher()
except ValueError as e:
    print("Livre refuse :", e)