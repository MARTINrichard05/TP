debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
elif debut > fin:
    print("Attention ! le début de la location est après la fin ...")
else:
    total = 0
    heures1 = 0
    heures2 = 0
    print("Vous avez loué votre vélo pendant")
    for i in range(debut, fin):
        if i < 7 or i >= 17:
            heures1 += 1
            total += 1
        else:
            heures2 += 1
            total += 2

    if heures1 > 0:
        print("%d heure(s) au tarif horaire de 1.0 euro(s)" % heures1)

    if heures2 > 0:
        print("%d heure(s) au tarif horaire de 2.0 euro(s)" % heures2)

    print("Le montant total à payer est de %d euro(s)." % total)
