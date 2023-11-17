nb = [-2,0.1,4,1.5,-1,-9,3,1.2,2.9,0,-20]

def test(x):
    if x < 3 and not x < 2:
        print(x, "x appartient à I")
    elif not x <= 0 and x <= 1:
        print(x,"x appartient à I")
    elif not x < -10 and x <= -2:
        print(x,"x appartient à I")
    else:
        print(x,"x n'appartient pas à I")

for i in nb:
    test(i)

