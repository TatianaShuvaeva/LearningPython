def verdoppeln(wert):
    return wert * 2
print(verdoppeln(5))

liste = [12,45,67, 89]
for i in liste:
    print(verdoppeln(i)) 

ergebnis = map(verdoppeln, liste)
print(ergebnis)
for i in ergebnis:
    print(i)
    
ergebnis_b = list(map((lambda x:2 * x), liste))
print(ergebnis_b)
for i in ergebnis:
    print(i)