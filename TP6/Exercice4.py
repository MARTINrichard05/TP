import random

def generer(nbr, vmin, vmax):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(vmin, vmax))
    return tab

def combienInferieur(table, vseuil):
    total = 0
    for i in table:
        if i < vseuil:
            total += 1
    return total


nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")

# b
nb = int(input("Combien de nombres entiers voulez-vous générer ? "))
vmin = int(input("Quelle est la valeur minimale ? "))
vmax = int(input("Quelle est la valeur maximale ? "))
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
seuil = input("Voulez-vous préciser le seuil ? ")
if seuil == "Oui" or seuil == "O":
    vseuil = int(input("Quel est le seuil ? "))
else:
    vseuil = 30
total = combienInferieur(tab, vseuil)
print(f"Il y en a {total} inférieurs à {vseuil}")
