kreditkartennummer = '9342571866701996'
liste_verdoppelung = []
summe = 0
quersumme = 0
differenz = 0
pruefziffer = 0
list_ziffern = list(kreditkartennummer)
for i in range(len(list_ziffern)-2, -1, -2):
    a = int(list_ziffern[i])*2
    liste_verdoppelung.append(a)
for i in range(1, len(list_ziffern)-2, 2): 
    c = int(list_ziffern[i]) 
    liste_verdoppelung.append(c)
print(liste_verdoppelung)    


for i in liste_verdoppelung:
   
    element = i
    if element > 9:
        element_in_str = str(element)
        for i in range(len(element_in_str)):
            b = int(element_in_str[i])
            quersumme += b
#print(summe_elementen)
    else:
        summe += i
summe = summe + quersumme
print(summe)

kleinere_zahl = summe
while kleinere_zahl % 10 != 0:
    kleinere_zahl -= 1
differenz = summe - kleinere_zahl
pruefziffer = 10 - differenz
print(pruefziffer) 

#if pruefziffer == 
