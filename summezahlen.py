z = int(input())
sum_zahl = z
quadratzahl=z*z
if sum_zahl == 0:
    print(sum_zahl)
else:
    while sum_zahl != 0:
        z = int(input())
        sum_zahl += z 
        neuquadratzahl = z*z  
        quadratzahl += neuquadratzahl
    print(quadratzahl)                
    

