import os
from helfer.bearbeiter import Bearbeiter

ordnerpfad = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print('ordner: ' + ordnerpfad)

liste_file = ('daten.txt', 'daten2.txt')
for file in liste_file:
    Bearbeiter.verarbeiten_file(ordnerpfad, file)
