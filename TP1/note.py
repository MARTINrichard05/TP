# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
nom = "Martin"
prenom = "Richard"
math = 15
anglais = 18
info = 16
moyenne = (math + anglais + info) / 3
promotion = 2023

print("Bonjour " + prenom + " " + nom + " de la promotion " + str(promotion))
print("Votre moyenne est de " + str(moyenne))
print("Votre pire note est " + str(min(math, anglais, info)))
print("Votre meilleure note est " + str(max(math, anglais, info)))