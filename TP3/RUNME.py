# un selecteur de programme, on demande le choix a l'utilisateur et on execute le fichier correspondant
#


while True:
    print("Choisissez un exercice :")
    print("1 : Choix de la structure itérative")
    print("2 : nombre 100")
    print("3 : Jeu du nombre mystère")
    print("4 : Factorielle itérative")
    print("5 : Location de vélos")
    print("d : Tous les exercices 1 par 1")
    print("q : Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        import ex1
    elif choix == "2":
        import ex2
    elif choix == "3":
        import ex3
    elif choix == "4":
        import ex4
    elif choix == "5":
        import Velo
    elif choix == "d":
        import ex1
        import ex2
        import ex3
        import ex4
        import Velo
    elif choix == "q":
        break
    else:
        print("Choix incorrect.")