import random

def generieren_passwort(anzahl_zeichen_passwort):
    passwort =''
    while anzahl_zeichen_passwort > 0:
        zufallzahl = random.randint(33,126)
        zufallzeichen = chr(zufallzahl)
        passwort = passwort + zufallzeichen
        anzahl_zeichen_passwort -= 1
    return passwort

anzahl_zeichen_passwort = int(input("Geben Sie bitte den Anzahl der Zeichen im Passwort ein: "))
passwort = generieren_passwort(anzahl_zeichen_passwort)
# print(f'Ihr generiertes Passwort: "{passwort}"')
print(f'Ihr generiertes Passwort: {passwort}')

# anzahl_zeichen_passwort = 1000
# ergebnis = generieren_passwort(anzahl_zeichen_passwort)
# assert len(ergebnis) == anzahl_zeichen_passwort, 'Funktion funktioniert falsch'

# anzahl_zeichen_passwort = -1
# ergebnis = generieren_passwort(anzahl_zeichen_passwort)
# assert len(ergebnis) == 0, 'Funktion funktioniert falsch'

# ergebnis = generieren_passwort(0)
# assert len(ergebnis) == 0, 'Funktion funktioniert falsch'
