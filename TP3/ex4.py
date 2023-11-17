n = int(input("Saisir un entier : "))
fact = 1
for i in range(1, n+1):
    fact *= i
    print("La factorielle de %d est %d." % (i, fact))