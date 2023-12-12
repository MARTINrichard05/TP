nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")
nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

if nom1.lower() < nom2.lower():
    print(prenom1.capitalize(), nom1.upper())
    print(prenom2.capitalize(), nom2.upper())
elif nom1.lower() > nom2.lower():
    print(prenom2.capitalize(), nom2.upper())
    print(prenom1.capitalize(), nom1.upper())
else:
    if prenom1.lower() < prenom2.lower():
        print(prenom1.capitalize(), nom1.upper())
        print(prenom2.capitalize(), nom2.upper())
    else:
        print(prenom2.capitalize(), nom2.upper())
        print(prenom1.capitalize(), nom1.upper())

