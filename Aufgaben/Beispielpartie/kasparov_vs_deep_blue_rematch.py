import os

ordnerpfad = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print('ordner: ' + ordnerpfad)

path_to_file = os.path.join(ordnerpfad, 'daten.txt')
print(path_to_file)

file_input = open(path_to_file)
for line in file_input:

