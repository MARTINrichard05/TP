# tire une valeur aléatoire x entre 0 et 100 et qui demande à l’utilisateur de deviner cette valeur. L’algorithme répond à chaque fois si la valeur est plus grande, plus petite ou égale à la valeur à deviner. Un compteur incrémenté à chaque passage donnera le nombre de tours qui ont été nécessaires pour trouver le nombre mystère.

from random import randint

nb_mystr = randint(0, 100)
nb_user = int(input("Saisir un entier entre 0 et 100 : "))
nb_tour = 1
while nb_user != nb_mystr:
    if nb_user < nb_mystr:
        print("Le nombre mystère est plus grand.")
    else:
        print("Le nombre mystère est plus petit.")
    nb_user = int(input("Saisir un entier entre 0 et 100 : "))
    nb_tour += 1
print("Bravo, vous avez trouvé le nombre mystère en %d tours." % nb_tour)

