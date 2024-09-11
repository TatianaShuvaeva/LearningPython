import time
from functools import cache


@cache
def fibonacci_fakultaeten(n):
    if n < 2:
        return n
    return fibonacci_fakultaeten(n - 1) + fibonacci_fakultaeten(n - 2)


def erstellen_fakultaeten(anzahl_studenten_uni):
    liste_fakultaeten = []
    studenten_fakultaeten = 0
    n = 0
    while studenten_fakultaeten <= anzahl_studenten_uni:
        studenten = fibonacci_fakultaeten(n)
        if studenten_fakultaeten + studenten > anzahl_studenten_uni:
            break
        liste_fakultaeten.append(studenten)
        studenten_fakultaeten += studenten
        n += 1

    return liste_fakultaeten, studenten_fakultaeten

anzahl_studenten_uni = 1000
liste_fakultaeten, studenten_fakultaeten = erstellen_fakultaeten(anzahl_studenten_uni)

print(f"An der Uni wurden Fakultäten {liste_fakultaeten} mit einer Gesamtzahl von Studenten {studenten_fakultaeten} geschaffen")
        