import datetime

year = datetime.date.today().year

age = int(input("Donnez votre âge: "))
print(age)
if age < 0:
    print("Vous n'êtes pas encore né!")
annee = year - age
print("Votre année de naissance est : " + str(annee))