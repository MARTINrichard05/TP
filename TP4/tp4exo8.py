
dico = {"firstname": "richard", "name": "Martin", "promo": "2023", "group": "121"}

print("votre nom est", dico["name"], ", prénom est", dico["firstname"], ", vous faites partie de la promo", dico["promo"], "et votre groupe est", dico["group"])

print("Les clés du dictionnaire sont :")
for i in dico.keys():
    print("-", i)

print("Les valeurs du dictionnaire sont :")
for i in dico.values():
    print("-", i)

print("Les tuplets du dictionnaire sont :")
for i in dico.items():
    print("-", i)

binome = {"login1": dico, "login2": {"firstname": "Jeff", "name": "Bezoce", "promo": "1956", "group": "564"}}

print("Les étudiants formants le binôme sont :")

for i in binome.values():
    print("- L'étudiant", i["firstname"], i["name"], "du groupe", i["group"])