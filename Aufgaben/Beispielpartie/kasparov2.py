import os
from helfer.bearbeiter import Bearbeiter

ordnerpfad = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print('ordner: ' + ordnerpfad)

liste_file = ('daten2.txt', 'daten.txt')
for file in liste_file:
    path_to_file = os.path.join(ordnerpfad, file)
    print(path_to_file)

    file_input = open(path_to_file)
    ergebnis = Bearbeiter.verarbeiten_file(file_input)
 
    metadaten, zuege_spiel = ergebnis
    print(metadaten)
    for idx, element in enumerate(zuege_spiel):  # Zweite bessere Variante 
        print(f"zuege[{idx}]={element}")