kanten = {
    ('A', 'B'): 20,
    ('A', 'D'): 5,
    ('D', 'E'): 6,
    ('E', 'B'): 2,
    ('A', 'C'): 8,
    ('C', 'B'): 9
}

routen = [
    ['A', 'B'],    
    ['A', 'C', 'B'],
    ['A', 'D', 'E', 'B']
]

def create_kanten(route):
    kanten = []
    for i in range(len(route)-1):
        kanten.append((route[i], route[i+1]))
    return kanten

def findeRoute(gewicht):
    index_routen = []
    for i in range(len(routen)):
    # print(routen[i])
        route_kanten = create_kanten(routen[i])
    # print(route_kanten)
    
        anzahl_kanten_bedingung = 0
    
        for k in route_kanten:
            if kanten[k] >= gewicht:
                anzahl_kanten_bedingung += 1

        if len(route_kanten) == anzahl_kanten_bedingung:
            index_routen.append(i)
    return index_routen

gewicht = 8
index_routen = findeRoute(gewicht)
print(index_routen)
