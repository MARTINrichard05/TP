from random import randint
# on lance une pièce avec un nombre entier aléatoire entre 0 et 100
piece = randint(0, 100)
if piece < 50:
    print("pile")
else:
    print("face")
