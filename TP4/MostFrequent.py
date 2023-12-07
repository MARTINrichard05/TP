L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

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
