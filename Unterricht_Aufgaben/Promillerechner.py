def berechnen_promille(mensch: str, masse: float, volumen: float, alkoholvolumenanteil: float) -> float:
    r_mann = 0.7
    r_frau = 0.6
    dichte = 0.8
    a = volumen * alkoholvolumenanteil * dichte

#     if mensch.lower() == "m":
#         c = round((a/(masse*r_mann)),2)

#     elif mensch.lower() == "f":
#         c = round((a/(masse*r_frau)),2)
#     return c

    if mensch == "m":
        return round((a/(masse*r_mann)),2)

    return round((a/(masse*r_frau)),2)


mensch = ""

while mensch != "m" and mensch != "f":
    mensch = str(input("Geben Sie bitte ein, sind Sie Frau (f) oder Mann (m)?: ")).lower()
    if mensch != "m" or mensch != "f":
        print(f'Sie haben falsch eingegeben, sind Sie Frau (f) oder Mann (m)?')    
        
masse = float(input("Geben Sie bitte Ihr Gewicht in kg ein:  "))
volumen = float(input("Geben Sie bitte die Menge des konsumierten Alkohol in ml ein:  "))
alkoholvolumenanteil = float(input("Geben Sie bitte den Alkoholgehalt Ihres Getränks in % ein:  "))

c = berechnen_promille(mensch, masse, volumen, alkoholvolumenanteil)
     
print(f'Ihr Promillewert beträgt {c}')
