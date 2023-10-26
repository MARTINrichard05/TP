jour = 0
heure = 0
minute = 0

def temps(jour, heure, minute):
    return jour*24*60 + heure*60 + minute

jour = int(input("Jour: "))
heure = int(input("Heure: "))
minute = int(input("Minute: "))
print("il c'est écoulé ",temps(jour, heure, minute), " minutes depuis le debut du mois")