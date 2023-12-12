chaine = input("Entrez une chaine de caractères : ")
taille = 0
voyelles = 0
occurrences = 0
for i in chaine:
    taille += 1
    if i in "aeiouy":
        voyelles += 1
    if i == "w":
        if chaine[taille:taille+4] == "agon":
            occurrences += 1
print("La taille de la chaine est de", taille, "caractères.")
print("Le pourcentage de voyelles est de", voyelles/taille*100, "%.")
if occurrences != 0:
    print("La chaine 'wagon' apparait", occurrences, "fois.")
else:
    print("La chaine 'wagon' n'apparait pas dans la chaine.")
