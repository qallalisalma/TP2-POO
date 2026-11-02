class Livre:
 pass 

l1 = Livre()
l1.titre = "La Boite a merveilles"
l1.auteur = "Sefrioui"
l1.annee = 1954

l2 = Livre()
l2.titre = "Le Passe simple"
l2.auteur = "Chraibi"
l2.annee = 1954

l3 = Livre()
l3.titre = "Clean Code"
l3.auteur = "Robert Martin"
l3.annee = 2008


print(f"{l1.titre} - {l1.auteur} ({l1.annee})")
print(f"{l2.titre} - {l2.auteur} ({l2.annee})")
print(f"{l3.titre} - {l3.auteur} ({l3.annee})")