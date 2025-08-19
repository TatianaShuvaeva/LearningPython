from datetime import date, time
from typing import List

class Flug:
    def __init__(self, id: str, flugDatum: date, abflugzeit: time, ankunftZeit: time, preis: float, freiePlaetze: int):
        self._id = id
        self._flugDatum = flugDatum
        self._abflugzeit = abflugzeit
        self._ankunftZeit = ankunftZeit
        self._preis = preis
        self._freiePlaetze = freiePlaetze

    
    def getId(self): return self._id
    def getFlugDatum(self): return self._flugDatum
    def getAbflugzeit(self): return self._abflugzeit
    def getAnkunftZeit(self): return self._ankunftZeit
    def getPreis(self): return self._preis
    def getFreiePlaetze(self): return self._freiePlaetze


def erstelleFluege(datum: date, plaetze: int, linien_fluege: List[Flug]) -> List[Flug]:
    
    auswahl_fluege = []


    for flug in linien_fluege:
        if flug.getFlugDatum() == datum and flug.getFreiePlaetze() >= plaetze:
            auswahl_fluege.append(flug)

    auswahl_fluege.sort(key=lambda f: f.getPreis())
    
    return auswahl_fluege


if __name__ == "__main__":
    
    linien = [
        Flug("LH123", date(2025, 8, 18), time(8, 0), time(10, 0), 120.0, 5),
        Flug("LH456", date(2025, 8, 18), time(12, 0), time(14, 0), 90.0, 2),
        Flug("LH789", date(2025, 8, 19), time(16, 0), time(18, 0), 150.0, 10),
        Flug("LH999", date(2025, 8, 18), time(20, 0), time(22, 0), 200.0, 8),
    ]

  
    result = erstelleFluege(date(2025, 8, 18), 3, linien)

    for f in result:
        print(f"{f.getId()} | {f.getFlugDatum()} | Preis: {f.getPreis()} | Plätze: {f.getFreiePlaetze()}")
