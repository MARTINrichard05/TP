# Ecrire le programme « tp4exo7.py » qui enregistre dans un « tuplet » nommé «
# binome » votre login et celui de votre voisin de tp. Vous afficherez les deux membres
# du binôme dans une chaine de caractères du type : « L’étudiant login1 est en
# binome avec l’étudiant login2 » où « login1 » et « login2 » sont respectivement les
# valeurs de chaque membre enregistré dans le tuplet « binome ».

binome = ("richard", "login2")
print("L’étudiant", binome[0], "est en binome avec l’étudiant", binome[1])

# Vous souhaitez changer à présent de binôme, proposez la saisie du nouveau login et
# modifier le second élément du tuplet « binome » en conséquence. Que constatezvous ?
try:
    binome[1] = input("Nouveau binome : ")
    print("L’étudiant", binome[0], "est en binome avec l’étudiant", binome[1])
except Exception as e:
    print(e)
# on ne peut pas modifier un tuplet
# . Essayez de supprimer le second élément de binôme à présent à l’aide de la fonction
# intégrée « del() » Que constatez-vous ?
try:
    del binome[1]
    print("L’étudiant", binome[0], "est en binome avec l’étudiant", binome[1])
except Exception as e:
    print(e)
# on ne peut pas supprimer un élément d'un tuplet

# Vous souhaitez former un trinôme en ajoutant un troisième élément au « tuplet
# binome ». Comment procéder ? Que pouvez-vous en conclure sur les « tuplet » et
# leurs domaines d’utilisation ?
binome = binome + ("login3",)
print("L’étudiant", binome[0], "est en binome avec l’étudiant", binome[1], "et", binome[2])
# on peut ajouter un élément à un tuplet
# Les tuples sont des listes non modifiables, on ne peut pas ajouter, modifier ou supprimer un élément d'un tuplet, ils
# peuvent servir à stocker des données qui ne doivent pas être modifiées ou a passer des arguments à une fonction sans
# risque de les modifier.
