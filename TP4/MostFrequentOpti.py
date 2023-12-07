L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
#sortie : Le nombre le plus frequent dans la liste est le : 7 (3 x)
# on va utiliser count()

max=0
maxkey=0
for i in L1:
    cnt=L1.count(i)
    if cnt>max:
        max=cnt
        maxkey=i

print("Le nombre le plus frequent dans la liste est le :",maxkey,"(",max,"x)")



""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
