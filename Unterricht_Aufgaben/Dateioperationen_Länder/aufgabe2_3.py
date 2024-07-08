import os
from datei_einlesen import get_länder

# Aufgabe 2
def erstellen_länder_hauptstädte() -> dict[str, str]:
    länder_hauptstädte = {}

    länder = get_länder()
    for land in länder:
        hauptstadt = input(f"Geben Sie bitte die Hauptstadt von {land} ein: ")
    
    # TODO Überprüfen, dass hauptstadt string hat
    länder_hauptstädte[land] = hauptstadt.strip()
    return länder_hauptstädte

# länder_hauptstädte = erstellen_länder_hauptstädte()
länder_hauptstädte = {"Italien":"Rom", "Frankreich":"Paris", "Spanien":"Madrid", "Belgien":"Bruessel"}
#print(länder_hauptstädte)

# Aufgabe 3

anzahl_länder = 2
anzahl = 0
while anzahl < anzahl_länder:
    landneu = input(f"Geben Sie bitte ein neues Land ein: ")
    hauptstadtneu = input(f"Geben Sie bitte die Hauptstadt von {landneu} ein: ")
    # TODO Bei der Überprüfung von Ländern und Hauptstädten sollte die Groß-/Kleinschreibeung nicht beachtet werden
    if landneu in länder_hauptstädte:
        print(f"Leider gibt es dieses Land - {landneu} bereits in Länderliste")
    else:
        länder_hauptstädte[landneu] = hauptstadtneu.strip()
        anzahl +=1
# print(länder_hauptstädte)


ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_to_file = os.path.join(ordnerpfad, "länder_hauptstädte.txt")

try:
    with open(path_to_file, "w") as datei:
        for land in länder_hauptstädte:
            
            datei.write(f"{land} {länder_hauptstädte[land]}\n")
            
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except Exception as err:
    print("Sonstige Dateifehler", err)
    exit(100)
            