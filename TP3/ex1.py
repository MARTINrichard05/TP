
def a(n):
    somme = 0
    for i in range(n+1):
        somme += i
    print("La somme des %d premiers entiers naturels est %d." % (n, somme))

def b(n):
    while True:
        if int(input("Saisir un entier : ")) == 100:
            break
def c():
    val = []
    for i in range(10):
        while True:
            valt = float(input("Saisir une valeur réelle comprise entre 0 et 20 : "))
            if 0 <= valt <= 20:
                val.append(valt)
                break
            else:
                print("Valeur incorrecte.")
    print("\n \n")
    for i in range(10):
        if val[i] < 10:
            print(val[i], "est inférieure strictement à 10.")
        elif val[i] < 15:
            print(val[i], "est supérieure ou égale à 10 et inférieure strictement à 15.")
        else:
            print(val[i], "est supérieure ou égale à 15.")
def d(n):
    nombre = 0
    somme = 0
    while somme <= n:
        nombre += 1
        somme += nombre
    print("Le plus grand nombre N tel que ∑𝑁 𝑖=0 𝑖 ≤ %d est %d." % (n, nombre-1))

print("Choisissez un exercice :")
print("a : somme des n premiers entiers naturels.")
print("b : saisir des entiers jusqu'à ce que 100 soit saisi.")
print("c : saisir 10 réels entre 0 et 20 et les classer en catégories.")
print("d : déterminer le plus grand nombre N tel que ∑𝑁 𝑖=0 𝑖 ≤ n.")
print("tt : tester tous les exercices.")

while True:
    choix = input("Votre choix : ")
    if choix == "a":
        a(int(input("Saisir un entier : ")))
        break
    elif choix == "b":
        b(int(input("Saisir un entier : ")))
        break
    elif choix == "c":
        c()
        break
    elif choix == "d":
        d(int(input("Saisir un entier : ")))
        break
    elif choix == "tt":
        print("Exo a : somme des n entiers naturels.")
        print("\n \n")
        a(int(input("Saisir un entier : ")))
        print("\n \n")
        print("Exo b : saisir des entiers jusqu'à ce que 100 soit saisi.")
        print("\n \n")
        b(int(input("Saisir un entier : ")))
        print("\n \n")
        print("Exo c : saisir 10 réels entre 0 et 20 et les classer en catégories.")
        print("\n \n")
        c()
        print("\n \n")
        print("Exo d : déterminer le plus grand nombre N tel que ∑𝑁 𝑖=0 𝑖 ≤ n.")
        print("\n \n")
        d(int(input("Saisir un entier : ")))
        break
    else:
        print("Choix incorrect.")
