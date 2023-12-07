date_valide= False
while not date_valide:
    datestr = input("Donnez une date sous la forme jjmmaaaa : ")
    if len(datestr) != 8:
        print("Erreur de saisie : la date doit être sous la forme jjmmaaaa")
    else:
        jour = int(datestr[0:2])
        mois = int(datestr[2:4])
        annee = int(datestr[4:8])

        if mois < 1 or mois > 12:
            print("Erreur de saisie : le mois doit être compris entre 1 et 12")
        else:
            if mois == 2:
                if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
                    if jour < 1 or jour > 29:
                        print("Erreur de saisie : le jour doit être compris entre 1 et 29")
                    else:
                        print("Date valide")
                        date_valide = True
                else:
                    if jour < 1 or jour > 28:
                        print("Erreur de saisie : le jour doit être compris entre 1 et 28")
                    else:
                        print("Date valide")
                        date_valide = True
            else:
                if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
                    if jour < 1 or jour > 31:
                        print("Erreur de saisie : le jour doit être compris entre 1 et 31")
                    else:
                        print("Date valide")
                        date_valide = True
                else:
                    if jour < 1 or jour > 30:
                        print("Erreur de saisie : le jour doit être compris entre 1 et 30")
                    else:
                        print("Date valide")
                        date_valide = True