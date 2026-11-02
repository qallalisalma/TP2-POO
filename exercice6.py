class Livre:
    nombre_livres = 0

    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        Livre.nombre_livres = Livre.nombre_livres + 1
        self.numero = Livre.nombre_livres

    def afficher(self):
        print(f"#{self.numero} {self.titre} - {self.auteur} ({self.annee})")
print("Livres crees :", Livre.nombre_livres)
l1 = Livre("La Boite a merveilles", "Sefrioui", 1954)
l2 = Livre("Le Passe simple", "Chraibi", 1954)
l3 = Livre("Clean Code", "Martin", 2008)

l1.afficher()
l2.afficher()
l3.afficher()

print("Livres crees :", Livre.nombre_livres)