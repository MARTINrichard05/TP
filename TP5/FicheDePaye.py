nombreHeures = int(input("Entrez le nombre d'heures travaillées : "))
salaireHoraire = float(input("Entrez le salaire horaire : "))
salaire = 0
if nombreHeures <= 160:
    salaire = nombreHeures * salaireHoraire
elif nombreHeures <= 200:
    salaire = 160 * salaireHoraire + (nombreHeures - 160) * salaireHoraire * 1.25
else:
    salaire = 160 * salaireHoraire + 40 * salaireHoraire * 1.25 + (nombreHeures - 200) * salaireHoraire * 1.5
print("Le salaire est de", salaire)