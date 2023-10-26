x = int(input("Entrez x: "))
y = int(input("Entrez y: "))
print(" ")

print("Avant permutation:")
print("x : " + str(x))
print("y : " + str(y))
print(" ")

# Permutation
temp = x
x = y
y = temp


print("Après permutation:")
print("x : " + str(x))
print("y : " + str(y))