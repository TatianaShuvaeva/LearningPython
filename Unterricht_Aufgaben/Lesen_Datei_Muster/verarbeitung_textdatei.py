import os

ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_to_file = os.path.join(ordnerpfad, "test.txt")


try:
    eingabe_datei = open(path_to_file, "r")
    zeilen = eingabe_datei.readlines()
    eingabe_datei.close()
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except:
    print("sonstige Dateifehler")
    exit(100)
# Verarbeitung
print(zeilen)   
print(type(zeilen))
print(len(zeilen))
    

# for zeile in eingabe_datei:
#     print(zeile, end = "")
# z = "eins\nzwei\drei\nvier"
# print(z)
for z in zeilen:
    # if z.isalpha():
    if "n" in z:
        pass
    else:
        print(z, end = "")

