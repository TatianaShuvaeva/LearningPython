import os

ordnerpfad = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print('ordner: ' + ordnerpfad)

path_to_file = os.path.join(ordnerpfad, 'daten.txt')
print(path_to_file)

file_input = open(path_to_file)
metadaten = {}
line_number = 1
games = ''
line_number = 1
games = ''
for line in file_input:
    if line_number < 10:
        line_neu = line.strip('][\n') #Entfernt man eckige Klammern und Zeilenumbrüche
        line_split = line_neu.split(' ', maxsplit=1) #Teilt man die Zeichenfolge mit Leerzeichen als Trennzeichen auf
        key = line_split[0]
        value = line_split[1].strip('"')
        metadaten[key] = value
    elif line_number > 10:
        games_ohne = line.strip('\n') #Entfernt man Zeilenumbrüche
        # games += games_ohne
        games = games + ' ' + games_ohne   #Fügt man die Zeilen zu einer zusammen und fügt man ein Leerzeichen dazwischen ein'

    line_number += 1
    
games_split = games.split() #Teilt man eine Zeile mit einem Leerzeichen


games_refined = ''
for i in games_split:
    for s in i:
        if  s.isdigit() is True:    #Überprüft man, ob es Ziffern in jedem Elementgibt
            games_refined = games_refined + ' '+ i # Entfernt man {Kasparov schüttelt kurz den Kopf}
            break
    
# for e in games_refined: 
games_element = games_refined.split()
# print(games_element)
# zuege_spiel = []
# for i in games_element:
#     igames_element = i.split('.')
#     for i in games_element:
#         if len(i) == 2:
#             zuege_spiel = zuege_spiel + ' ' + i[1]
#         else:
#             zuege_spiel = zuege_spiel + ' ' + i[0]

    
#     print(zuege_spiel)
# print(metadaten)
    #  igames_element = i.split('.')

#  '1.e4'.split('.')
# ['1', 'e4']
# 'c6'.split('.')
# ['c6']
# games_result = ['e4']
# print(metadaten)

