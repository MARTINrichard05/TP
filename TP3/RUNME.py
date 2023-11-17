from time import sleep

while True:
    print("Choisissez un exercice :")
    print("1 : Choix de la structure itérative")
    print("2 : Compte à rebours")
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
        print("\n \n Exo 1 : Choix de la structure itérative \n")
        sleep(0.5)
        import ex1
        sleep(1.5)
        print("\n \n Exo 2 : Compte à rebours \n")
        sleep(0.5)
        import ex2
        sleep(1.5)
        print("\n \n Exo 3 : Jeu du nombre mystère \n")
        sleep(0.5)
        import ex3
        sleep(1.5)
        print("\n \n Exo 4 : Factorielle itérative \n")
        sleep(0.5)
        import ex4
        sleep(1.5)
        print("\n \n Exo 5 : Location de vélos \n")
        sleep(0.5)
        import Velo
        sleep(1.5)
    elif choix == "q":
        break
    else:
        print("Choix incorrect.")