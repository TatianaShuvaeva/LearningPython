reihe = 6
m = (2*reihe) - 2
for i in range(0,reihe):
    for j in range(0,m):
        print(end =" ")
    m = m -1
    for k in range(0, i + 1):
        print("*", end = "  ")
    print(" ")