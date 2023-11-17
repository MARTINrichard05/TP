from time import sleep
def version_for():
    n = int(input("Saisir un nombre entier positif : "))
    for i in range(n, -1, -1):
        print(i)
        sleep(0.5)

def version_while():
    n = int(input("Saisir un nombre entier positif : "))
    while n >= 0:
        print(n)
        n -= 1
        sleep(0.5)


while True:
    print("Choisissez une version :")
    print("a : boucle for")
    print("b : boucle while")
    print("q : quitter")
    choix = input("Votre choix : ")
    if choix == "a":
        version_for()
    elif choix == "b":
        version_while()
    elif choix == "q":
        break
    else:
        print("Choix incorrect.")