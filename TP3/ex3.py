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

