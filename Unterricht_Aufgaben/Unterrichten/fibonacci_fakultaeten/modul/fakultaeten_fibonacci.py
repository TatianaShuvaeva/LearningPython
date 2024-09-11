from typing import List


def _fibonacci_fakultaeten(n) -> int:
    if n < 2:
        return n
    return _fibonacci_fakultaeten(n - 1) + _fibonacci_fakultaeten(n - 2)


def erstellen_fakultaeten(anzahl_studenten_uni: int) -> tuple[List[int], int]:
    if not isinstance(anzahl_studenten_uni, int) or anzahl_studenten_uni < 0:
        raise ValueError("anzahl_studenten_uni muss integer und positiv sein")

    liste_fakultaeten: List[int] = []
    studenten_fakultaeten: int = 0
    n = 0

    while True:
        studenten = _fibonacci_fakultaeten(n)
        if studenten_fakultaeten + studenten > anzahl_studenten_uni:
            break
        liste_fakultaeten.append(studenten)
        studenten_fakultaeten += studenten
        n += 1

    return liste_fakultaeten, studenten_fakultaeten
