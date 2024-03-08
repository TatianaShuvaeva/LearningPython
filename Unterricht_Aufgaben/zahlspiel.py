from random import *
zahl = randint(1, 100)
i = 0
while i < 10:
    userZahl = int(input('Geben Sie bitte eine Zahl ein '))
    if userZahl > zahl:
        i += 1
        print('Ihre Zahl zu hoch')
    elif userZahl < zahl:
        i += 1
        print('Ihre Zahl zu niedrig')
    else:
        print('Toll! Sie erraten eine Zahl!')
print('Leider haben Sie die maximale Anzahl von Versuchen :()')
