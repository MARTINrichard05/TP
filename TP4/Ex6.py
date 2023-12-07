
n = [5, 2, 4, 8, 1, 3]

print(n)
for i in range(0, len(n)):
    for j in range(i+1, len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
    print(n)

# si je fait  print(sorted(tab)) on m'affiche la liste triée (mais pas modifiée)
# si je fait tab.sort() on modifie la liste