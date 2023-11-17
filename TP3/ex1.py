
def a(n):
    somme = 0
    for i in range(n+1):
        somme += i
    print("La somme des %d premiers entiers naturels est %d." % (n, somme))

def b(n):
    while True:
        if int(input("Saisir un entier : ")) == 100:
            break