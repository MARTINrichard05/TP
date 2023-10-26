from random import randint
# on lance une pièce truquée(dans 2/3 des cas on a pile) avec un nombre entier aléatoire entre 0 et 100
piece = randint(0, 100)
if piece < 66:
    print("pile")
else:
    print("face")
