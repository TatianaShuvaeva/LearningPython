import os

current_directory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

path_to_file = os.path.join(current_directory, 'words.txt')
file_input = open(path_to_file)


for line in file_input:
    word = line.strip()
    if len(word) > 20:
        print(word)
        