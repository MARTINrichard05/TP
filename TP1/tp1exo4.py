# l'utilisateur entre le nombre de minutes depuis le debut du mois et le script calcule le jour, l'heure , la minute
minutes_total = int(input("nombre de minutes total : "))

def calcul(minutes_tot):
    jours = minutes_tot // 1440
    minutes_tot -= jours * 1440
    heures = minutes_tot // 60
    minutes_tot -= heures * 60
    return {'jours': jours, 'heures' : heures, 'minutes': minutes_tot}

print(calcul(minutes_total))