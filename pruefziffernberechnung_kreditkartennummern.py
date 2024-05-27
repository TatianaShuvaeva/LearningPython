kreditkartennummer = '123456789'
liste_verdoppelung= []
quersumme = 0
#ziffern = [int(i) for i in kreditkartennummer.split()]
list_ziffern = list(kreditkartennummer)
for i in range(len(list_ziffern)-2,-1,-2):
    a = int(list_ziffern[i])*2
    liste_verdoppelung.append(a)
for i in liste_verdoppelung:
    if liste_verdoppelung[i] < 9:
        quersumme = liste_verdoppelung[i]
    else:
        for 

print(liste_verdoppelung)
#ziffern = [int(i) for i in kreditkartennummer.split()]


