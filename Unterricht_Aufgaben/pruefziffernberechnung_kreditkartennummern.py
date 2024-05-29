# kreditkartennummer = '9342571866701996'
# liste_verdoppelung = []
# summe = 0
# quersumme = 0
# differenz = 0
# ergebnis = 0
# list_ziffern = list(kreditkartennummer)
# for i in range(len(list_ziffern)-2, -1, -2):
#     a = int(list_ziffern[i])*2
#     liste_verdoppelung.append(a)
# for i in range(1, len(list_ziffern)-2, 2): 
#     c = int(list_ziffern[i]) 
#     liste_verdoppelung.append(c)
# print(liste_verdoppelung)    


# for i in liste_verdoppelung:
   
#     element = i
#     if element > 9:
#         element_in_str = str(element)
#         for i in range(len(element_in_str)):
#             b = int(element_in_str[i])
#             quersumme += b
# #print(summe_elementen)
#     else:
#         summe += i
# summe = summe + quersumme
# print(summe)

# kleinere_zahl = summe
# while kleinere_zahl % 10 != 0:
#     kleinere_zahl -= 1
# differenz = summe - kleinere_zahl
# ergebnis = 10 - differenz
# print(ergebnis) 

# pruefziffern = kreditkartennummer[-1]
# if ergebnis == int(pruefziffern):
#     print("Nummer gültig")   
# else:
#     print("Nummer ungültig")

#########################################

# kreditkartennummer = '9342571866701996'
# liste_verdoppelung = []
# summe = 0
# differenz = 0
# ergebnis = 0
# list_ziffern = list(kreditkartennummer)
# # nummer = [int(x) for x in kartennummer]
# for i in range(0, len(list_ziffern), 2):
#     verdoppelt = int(list_ziffern[i])*2
#     liste_verdoppelung.append(verdoppelt)
#     if verdoppelt > 9:
#         verdoppelt = verdoppelt - 9 
#     summe += verdoppelt
    
# for i in range(1, len(list_ziffern)-2, 2): 
#     c = int(list_ziffern[i]) 
#     liste_verdoppelung.append(c)
#     summe += c
# # print(summe)    


# zahl_durch_zehn = summe
# while zahl_durch_zehn % 10 != 0:
#     zahl_durch_zehn -= 1
# differenz = summe - zahl_durch_zehn
# ergebnis = 10 - differenz
# # print(ergebnis) 

# pruefziffern = kreditkartennummer[-1]
# if ergebnis == int(pruefziffern):
#     print("Nummer gültig")   
# else:
#     print("Nummer ungültig")

#######################################

kreditkartennummer = '9342571866701996'
liste_verdoppelung = []
summe = 0

list_ziffern = list(kreditkartennummer)

for i in range(len(list_ziffern)- 1):
    symbol_int = int(list_ziffern[i])
    if i %2 == 0:
        verdoppelt = symbol_int*2
        liste_verdoppelung.append(verdoppelt)
        if verdoppelt > 9:
            verdoppelt = verdoppelt - 9 
        summe += verdoppelt
    else: 
        liste_verdoppelung.append(symbol_int)
        summe += symbol_int
# print(summe)    

differenz = summe % 10
ergebnis = 10 - differenz
# print(ergebnis) 

pruefziffern = kreditkartennummer[-1]
if ergebnis == int(pruefziffern):
    print("Nummer gültig")   
else:
    print("Nummer ungültig")