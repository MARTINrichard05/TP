def version_for():
    n = int(input("Saisir un nombre entier positif : "))
    for i in range(n, -1, -1):
        print(i)

def version_while():
    n = int(input("Saisir un nombre entier positif : "))
    while n >= 0:
        print(n)
        n -= 1