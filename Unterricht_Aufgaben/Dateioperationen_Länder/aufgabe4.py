import os
from datei_einlesen import get_länder, get_länder_hauptstädte

try:
    länder = get_länder()
    länder_hauptstädte = get_länder_hauptstädte()
    abgleich_länder = []
    for land_hauptstadt in länder_hauptstädte:
        land = land_hauptstadt.split(' ') # Element nach Leerzeichen aufteilen
        if land[0] not in länder:
            abgleich_länder.append(land[0])
    print(f"Diese Länder gibt es nicht: {abgleich_länder}")

except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except Exception as err:
    print("Sonstige Dateifehler", err)
    exit(100) 
