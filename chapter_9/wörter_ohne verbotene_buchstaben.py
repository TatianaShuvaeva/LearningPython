import os

current_directory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

path_to_file = os.path.join(current_directory, 'words2.txt')
file_input = open(path_to_file)


def calculate_sum(file_input, forbidden):
    sum_wort_ohne = 0
    for letter in file_input:
        # if forbidden not in line:
        #      sum_wort_ohne += 1
        #      print(line)
        if avoids(letter) == False:
             wort_zahl_ohne += 1
             print(letter) 
    return sum_wort_ohne


def avoids(wort):
    if letter in forbidden:
        return True
    return False

    
forbidden = str(input('Geben Sie 5 verbotene Buchstaben ein  '))

wörter_ohne_verbotene_buchstaben = avoids(file_input, forbidden)
print('Summe der Wörter', wörter_ohne_verbotene_buchstaben)