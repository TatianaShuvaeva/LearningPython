import os

ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_to_file = os.path.join(ordnerpfad, "Länder.txt")

try:
    eingabe_datei = open(path_to_file, "r")
    for zeile in eingabe_datei:
        print(zeile, end = "")
    eingabe_datei.close()
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except:
    print("sonstige Dateifehler")
    exit(100)