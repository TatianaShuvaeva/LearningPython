# anzahl = 11
# stern = "*"
# while len(stern)<= anzahl:
#     print(stern)
#     stern  += "**"

#  Aufgabe 1

# höhe = 6
# i = 1
# stern = "*"
# leerzeichen = "1" * höhe
# while i <= höhe and len(stern) <= :
#     print(f"{leerzeichen}{stern}")
#     leerzeichen = leerzeichen[:1] + leerzeichen[2:]
#     stern += "**"
#     i += 1
#print(leerzeichen*5+stern[:3]+leerzeichen*5)

#  Aufgabe 2

höhe = int(input("Geben Sie bitte die Höhe des Weihnachtsbaum ein (ohne Stamm): "))
breite = int(input("Geben Sie bitte die Breite des Weihnachtsbaum ein (ungerade Zahl): "))
i = 1
stern = "*"
leerzeichen = "1" * höhe
while i <= höhe and len(stern) <= breite:
    print(f"{leerzeichen}{stern}")
    leerzeichen = leerzeichen[:1] + leerzeichen[2:]
    stern += "**"
    i += 1

#print(leerzeichen*5+stern[:3]+leerzeichen*5)

# 3 Version mit gerade und ungerade

# höhe = 3
# breite = 6
# i = 1
# stern = "*"
# leerzeichen = "1" * höhe
# if breite % 2 == 1:
#     while i <= höhe and len(stern) <= breite:
#         print(f"{leerzeichen}{stern}")
#         leerzeichen = leerzeichen[:1] + leerzeichen[2:]
#         stern += "**"
#         i += 1
# else:
#     m = (2*breite) - 2
#     for i in range(0,breite):
#         for j in range(0,m):
#             print(end =" ")
#         m = m -1
#         for k in range(0, i + 1):
#             print("*", end = " ")
#         print(" ")