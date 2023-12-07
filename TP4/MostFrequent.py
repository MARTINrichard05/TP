L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
#sortie : Le nombre le plus frequent dans la liste est le : 7 (3 x)
workingdict= {}
for i in L1:
    if i in workingdict:
        workingdict[i]+=1
    else:
        workingdict[i]=1
max=0
maxkey=0
for i in workingdict:
    if workingdict[i]>max:
        max=workingdict[i]
        maxkey=i
print("Le nombre le plus frequent dans la liste est le :",maxkey,"(",max,"x)")



""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
