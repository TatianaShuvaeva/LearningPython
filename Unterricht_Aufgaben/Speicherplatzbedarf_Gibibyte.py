# höhe = 0
# breite = 0
# speicherbedarf = 0
# anzahl_bilder = 0

# while höhe <= 0 or breite <= 0 or speicherbedarf <=0 or anzahl_bilder <=0:  # Beginn einer Schleife, die nur durch ein break beendet

#     if höhe <= 0:  # Überprüfung, ob gültig ist
#         print("Die Höhe des Bildes sollte > 0 sein")
#         höhe = int(input("Bitte geben Sie die Höhe des Bildes ein: "))
        
#     if breite <= 0:  # Überprüfung, ob die elektrische Stromstärker gültig sind
#         print("Die Breite des Bildes sollten > 0 sein")
#         breite = int(input("Bitte geben Sie die Breite des Bildes ein: "))
    
#     if speicherbedarf <=0:
#         print("Der Speicherbedarf sollten > 0 sein")
#         speicherbedarf = int(input("Bitte geben Sie den Speicherbedarf ein: "))
        
#     if  anzahl_bilder <=0: 
#         print("Die Anzahl der Bilder sollten > 0 sein")
#         anzahl_bilder = int(input("Bitte geben Sie die Anzahl der Bilder ein: "))    
        

# speicherbedarf_byte = breite * höhe * speicherbedarf * anzahl_bilder
# speicherplatzbedarf_gibibyte = speicherbedarf_byte / (1024 ** 3)  # Umrechnung in Gibibyte
# print(f"Der Speicherplatzbedarf beträgt {speicherplatzbedarf_gibibyte} Gibibyte.")


höhe = int(input("Bitte geben Sie die Höhe des Bildes in Pixeln ein: "))
while höhe <= 0:
    print("Die Höhe des Bildes sollte > 0 sein")
    höhe = int(input("Bitte geben Sie die Höhe des Bildes in Pixeln  ein: "))
    
breite = int(input("Bitte geben Sie die Breite des Bildes in Pixeln ein: "))
while breite <= 0:
    print("Die Breite des Bildes sollten > 0 sein")
    breite = int(input("Bitte geben Sie die Breite des Bildes in Pixeln ein: "))

speicherbedarf = int(input("Bitte geben Sie den Speicherbedarf pro Pixel in Byte ein: "))
while speicherbedarf <=0:
    print("Der Speicherbedarf sollten > 0 sein")
    speicherbedarf = int(input("Bitte geben Sie den Speicherbedarf pro Pixel in Byte ein: "))
    
anzahl_bilder = int(input("Bitte geben Sie die Anzahl der Bilder ein: "))
while anzahl_bilder <=0: 
    print("Die Anzahl der Bilder sollten > 0 sein")
    anzahl_bilder = int(input("Bitte geben Sie die Anzahl der Bilder ein: "))
    
speicherbedarf_byte = breite * höhe * speicherbedarf * anzahl_bilder
speicherplatzbedarf_gibibyte = round(speicherbedarf_byte / (1024 ** 3)),2  # Umrechnung in Gibibyte
print(f"Der Speicherplatzbedarf beträgt {speicherplatzbedarf_gibibyte} Gibibyte.")

