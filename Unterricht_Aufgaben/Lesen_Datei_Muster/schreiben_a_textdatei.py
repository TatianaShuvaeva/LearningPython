import os

ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_to_file = os.path.join(ordnerpfad, "testneu.txt")

# Verarbeitung
zeilen = []
zeilen.append("hallo ")
zeilen.append("Welt\n")
zeilen.append("Guten Morgen")

try:
    ausgabe_datei = open(path_to_file, "w")
    
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except:
    print("sonstige Dateifehler")
    exit(100)


ausgabe_datei.writelines(zeilen)
ausgabe_datei.close()

