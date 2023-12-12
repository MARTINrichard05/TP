
vals = []

for i in range(5):
    vals.append(input("Veuillez entrer la note du module "+str(i)+" et le coefficient correspondant : ").split(" "))
    vals[i][0] = float(vals[i][0])
    vals[i][1] = int(vals[i][1])

moyenne = 0
coef = 0

for i in range(5):
    moyenne += vals[i][0]*vals[i][1]
    coef += vals[i][1]

moyenne /= coef

print("La moyenne est de", moyenne)


# L’étudiant est admis s’il a une moyenne générale supérieure à 10
# et si aucune de ses notes n’est inférieure à 8.

if moyenne > 10:
    if min([vals[i][0] for i in range(5)]) > 8:
        print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")

