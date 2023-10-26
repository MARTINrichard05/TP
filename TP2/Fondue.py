BASE = 4
fromage = 800.0
eau = 2.0
ail = 2.0
pain = 400.0

nbConvives = int(input("Entrez le nombre de presonne(s) conviées à la fondue : "))
print("Pour faire une fondue fribourgeoise pour " + str(nbConvives) + " personne(s), il vous faut :")
print("- "+str(fromage * nbConvives / BASE) + " gr de fromage")
print("- "+str(eau * nbConvives / BASE) + " dl d'eau")
print("- "+str(ail * nbConvives / BASE) + " gousse(s) d'ail")
print("- "+str(pain * nbConvives / BASE) + " gr de pain")
