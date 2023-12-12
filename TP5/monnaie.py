
somme = int(input("Entrez une somme d'argent : "))
billet100 = somme // 100
reste = somme % 100
billet50 = reste // 50
reste = reste % 50
billet10 = reste // 10
reste = reste % 10
piece2 = reste // 2
reste = reste % 2
piece1 = reste
print(somme, "euros, c'est donc", billet100, "billets de 100,", billet50, "billets de 50,", billet10, "billets de 10,", piece2, "pièces de 2 et", piece1, "pièces de 1.")