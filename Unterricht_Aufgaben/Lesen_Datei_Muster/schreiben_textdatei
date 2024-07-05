import os

ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_to_file = os.path.join(ordnerpfad, "testneu.txt")


try:
    ausgabe_datei = open(path_to_file, "w")
    
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except:
    print("sonstige Dateifehler")
    exit(100)
# Verarbeitung
zeile = "hallo\n"
ausgabe_datei.write(zeile)

# ausgabe_datei.close()

zeile = "Welt\n"
ausgabe_datei.write(zeile)


ausgabe_datei.write("Guten Morgen")