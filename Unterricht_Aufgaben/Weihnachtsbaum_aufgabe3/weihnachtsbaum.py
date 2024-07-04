import json
import os

ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_to_file = os.path.join(ordnerpfad, "parameter.json")


try:
    eingabe_datei = open(path_to_file, "r")
    parameter = json.load(eingabe_datei)
    breite = parameter["breite"]    
    höhe = parameter["höhe"]
except FileNotFoundError as ex:
    print(ex)
    

i = 1
stern = "*"
leerzeichen = " " * höhe
while i <= höhe and len(stern) <= breite:
    print(f"{leerzeichen}{stern}")
    leerzeichen = leerzeichen[:1] + leerzeichen[2:]
    stern += "**"
    i += 1

print(leerzeichen*(höhe-1)+stern[:3])
