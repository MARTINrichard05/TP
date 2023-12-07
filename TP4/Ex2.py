nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))

moyenne = 0.0
notes = []

for i in range(0, nombreEtudiants):
    note = float(input("Note etudiant " + str(i) + " : "))

    if note < 0 or note > 20:
        print("Note invalide ! \n Veuillez saisir une note entre 0 et 20")
    else:
        notes.append(note)
        moyenne += note

moyenne = round(moyenne/nombreEtudiants, 2)

print("Moyenne de classe : ", moyenne, "\n", "Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(0, nombreEtudiants):
    print(i, " | ", notes[i], " | ", notes[i] - moyenne)