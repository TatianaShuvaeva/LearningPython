# def vermeidet(wort, vervotenBuchstaben) -> str:
#     for letter in wort:
#         if letter in vervotenBuchstaben: 
#             return False
#     return True


# print(vermeidet('Sehenswürdigkeiten', 'azlxmb'))

import os

current_directory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

path_to_file = os.path.join(current_directory, 'words.txt')
file_input = open(path_to_file)

vervotenBuchstaben = str(input('Geben Sie bitte verbotene Buchstaben ein'))
AnzahlWörter = 0
for line in file_input:
    word = line.strip()
    for letter in wort:
#         if letter in vervotenBuchstaben:
        print(word)