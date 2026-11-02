class Livre:
    def __init__(self, titre, auteur, annee):
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
            etat = "emprunte"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")



original = Livre("Clean Code", "Martin", 2008)
meme = original                                          
copie = Livre(original.titre, original.auteur, original.annee)  

copie.emprunter()
print("Apres copie.emprunter() :")
print(" original : ", end=""); original.afficher()
print(" copie : ", end=""); copie.afficher()

meme.emprunter()
print("Apres meme.emprunter() :")
print(" original : ", end=""); original.afficher()

print(meme is original, copie is original)