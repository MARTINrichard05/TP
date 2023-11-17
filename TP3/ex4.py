#détermine la factorielle d’un entier n (donné par l’utilisateur) avec les deux types de boucles. Votre programme doit permettre à l’utilisateur de choisir la boucle à utiliser puis réalise le traitement nécessaire en conséquence.
#Votre programme doit permettre aussi l’affichage de l’évolution de la valeur de la factorielle à chaque itération !

n = int(input("Saisir un entier : "))
fact = 1
for i in range(1, n+1):
    fact *= i
    print("La factorielle de %d est %d." % (i, fact))