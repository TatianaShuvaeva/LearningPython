import os

current_directory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

path_to_file = os.path.join(current_directory, 'words.txt')
file_input = open(path_to_file)


# def has_no_letter(file_input, letter):
#     wort_zahl_ohne = 0
#     wort_zahl_mit = 0
#     for line in file_input:
#         if line.count(letter) == 0:
#              wort_zahl_ohne += 1
#              return line
#         else:
#             wort_zahl_mit += 1
#             sum = wort_zahl_ohne + wort_zahl_mit
#     prozent = wort_zahl_ohne/sum * 100
#     return prozent

# letter ='e'
# words_ohne = has_no_letter(file_input, letter)
# print(words_ohne)

def has_no_e(file_input):
    wort_zahl_ohne = 0
    wort_zahl_mit = 0
    sum = 0
    for line in file_input:
        if line.count('e') == 0:
             wort_zahl_ohne += 1
             print(line)
        else:
            wort_zahl_mit += 1
    sum = wort_zahl_ohne + wort_zahl_mit
    prozent = wort_zahl_ohne/sum * 100
    return prozent

prozent = has_no_e(file_input)


print(prozent) #33,074