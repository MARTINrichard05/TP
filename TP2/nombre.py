nombre = int(input("Entrez un nombre entier: "))


if nombre % 2 == 0:
    pair = "et pair"
if nombre % 2 == 1:
    pair = "et impair"
if nombre < 0:
    signe = "négatif"
if nombre > 0:
    signe = "positif"
if nombre == 0:
        signe = "zéro"
        pair = "(et il est pair)"

print("Le nombre est", signe, pair)