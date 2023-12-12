# Ecrire le script Verification.py permettant d’entrer le nom de deux fichiers. Si ces fichiers
# existent, le script donnera leurs tailles en octets. Le script indiquera ensuite quel est le fichier le
# plus récent (le fichier modifié le plus récemment) en affichant la date de modification.
# Pour cela, vous pouvez utiliser les fonctions du module « os.path » suivantes :
# ✓ os.path.isfile(path) : renvoie « True » si « path » est un fichier
# ✓ os.path.getmtime(path) : renvoie l’heure de la dernière modification du fichier
# donnée en paramètre. La valeur retournée est un nombre sous forme de timestamp
# représentant le nombre de secondes écoulées depuis le 1er janvier 1970 (l’Epoch
# Unix). Pour formater d’une manière plus lisible cette valeur, vous pouvez utiliser la
# datetime.datetime.fromtimestamp() en donnant en argument la date à
# formater. Vous devez pour cela importer le module ‘datetime’

import os.path
from datetime import datetime

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(fichier1):
    print("La taille du fichier", fichier1, "est de", os.path.getsize(fichier1), "octets.")
    print("Le fichier", fichier1, "a été modifié le", datetime.fromtimestamp(os.path.getmtime(fichier1)))
else:
    print("Le fichier", fichier1, "n'existe pas.")

if os.path.isfile(fichier2):
    print("La taille du fichier", fichier2, "est de", os.path.getsize(fichier2), "octets.")
    print("Le fichier", fichier2, "a été modifié le", datetime.fromtimestamp(os.path.getmtime(fichier2)))
else:
    print("Le fichier", fichier2, "n'existe pas.")
