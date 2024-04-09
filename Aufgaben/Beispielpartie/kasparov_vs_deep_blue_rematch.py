import os

ordnerpfad = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print('ordner: ' + ordnerpfad)

path_to_file = os.path.join(ordnerpfad, 'daten.txt')
print(path_to_file)

file_input = open(path_to_file)
metadaten = {}
for line in file_input:
    line_neu = line.strip('][\n')
    line_split = line_neu.split(' ', maxsplit=1)
    key = line_split[0]
    value = line_split[1].strip('"')
    metadaten[key] = value

print(metadaten)
