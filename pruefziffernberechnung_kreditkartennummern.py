kreditkartennummer = '123456789'
liste_verdoppelung = []
quersumme = 0
# ziffern = [int(i) for i in kreditkartennummer.split()]
list_ziffern = list(kreditkartennummer)
for i in range(len(list_ziffern)-2, -1, -2):
    a = int(list_ziffern[i])*2
    liste_verdoppelung.append(a)
print(liste_verdoppelung)

for i in liste_verdoppelung[i]:
    print(i)
    element = liste_verdoppelung[i]
    if element > 9:
        element_in_str = str(element)
        for i in element_in_str:
            print(i)


# ziffern = [int(i) for i in kreditkartennummer.split()]
