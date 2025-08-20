kanten: dict[tuple[str, str], dict[str, float]] = {
    ('A', 'B'): {
        "frachtkapazitaet": 20,
        "frachtkosten": 3
    },
    ('A', 'D'): {
        "frachtkapazitaet": 5,
        "frachtkosten": 1.3
    },
    ('D', 'E'): {
        "frachtkapazitaet": 6,
        "frachtkosten": 0.9
    },
    ('E', 'B'): {
        "frachtkapazitaet": 2,
        "frachtkosten": 2
    },
    ('A', 'C'): {
        "frachtkapazitaet": 8,
        "frachtkosten": 1.1
    },
    ('C', 'B'): {
        "frachtkapazitaet": 9,
        "frachtkosten": 1.2
    }
}

routen = [
    ['A', 'B'],    
    ['A', 'C', 'B'],
    ['A', 'D', 'E', 'B']
]

def create_kanten(route) ->  list[tuple[str, str]]:
    kanten = []
    for i in range(len(route)-1):
        kanten.append((route[i], route[i+1]))
    return kanten

def findeRouten(gewicht) -> list[tuple[int,float]]:
    guenstigste_routen: list[tuple[int, float]] = []
    for idx in range(len(routen)):
    # print(routen[i])
        route_kanten = create_kanten(routen[idx])
    # print(route_kanten)
    
        anzahl_kanten_bedingung = 0
        gesamtkosten = 0
        for k in route_kanten:
            
            kante = kanten[k]
            if kante['frachtkapazitaet'] >= gewicht:
                anzahl_kanten_bedingung += 1
                gesamtkosten += gewicht * kante['frachtkosten']
                
        if len(route_kanten) == anzahl_kanten_bedingung:
            guenstigste_routen.append((idx, gesamtkosten))

    return guenstigste_routen

def findeRoute(gewicht) -> int:
    guenstigste_routen = findeRouten(gewicht)
# print(guenstigste_routen)

    bester_preis = guenstigste_routen[0][1]
    bester_index = guenstigste_routen[0][0]
    for x in range(1, len(guenstigste_routen)):
        route = guenstigste_routen[x]
        route_preis = route[1]
        if bester_preis > route_preis:
            bester_preis = route_preis
            bester_index = route[0]
    return bester_index

gewicht = 8

bester_index = findeRoute(gewicht)
print(bester_index)
