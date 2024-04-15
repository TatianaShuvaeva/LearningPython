# höhe = int(input("Bitte geben Sie die Höhe des Bildes ein: "))
# if höhe <=0: 
#     print(f"Ihre Zahl: {höhe} sollte eine positive Zahl sein")

# breite = int(input("Bitte geben Sie die Breite des Bildes ein: "))
# if breite <=0: 
#     print(f"Ihre Zahl: {breite} sollte eine positive Zahl sein")
    
speicherbedarf = int(input("Bitte geben Sie den Speicherbedarf ein: "))
if speicherbedarf <=0: 
    print(f"Ihre Zahl: {speicherbedarf} sollte eine positive Zahl sein")
    
anzahl_bilder = int(input("Bitte geben Sie die Anzahl der Bilder ein: "))
if  anzahl_bilder <=0: 
    print(f"Ihre Zahl: {anzahl_bilder} sollte eine positive Zahl sein")
 

speicherbedarf_byte = breite * höhe * speicherbedarf * anzahl_bilder
speicherplatzbedarf_gibibyte = speicherbedarf_byte / (1024 ** 3)  # Umrechnung in Gibibyte
print(f"Der Speicherplatzbedarf beträgt {speicherplatzbedarf_gibibyte} Gibibyte.")
