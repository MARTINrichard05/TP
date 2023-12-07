nMax = 10
v1 = []
v2 = []

n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

while n < 1 or n > nMax:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

print("Saisie du premier vecteur :")
for i in range(0, n):
    v1.append(float(input("v1[" + str(i) + "] = ")))

print("\nSaisie du second vecteur :")
for i in range(0, n):
    v2.append(float(input("v2[" + str(i) + "] = ")))

produitScalaire = 0

for i in range(0, n):
    produitScalaire += v1[i] * v2[i]

print("\nLe produit scalaire de v1 par v2 vaut ", produitScalaire)