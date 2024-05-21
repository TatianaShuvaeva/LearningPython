def bestimmen_gehaltshöhe(betriebszugehörigkeit):
    if betriebszugehörigkeit < 5:
        gehalt = 1700
    elif betriebszugehörigkeit >= 5 and betriebszugehörigkeit < 10:
        gehalt = 2100
    else:
        gehalt = 2700
    return gehalt

    
def bestimmen_gehaltszuschlaghöhe(monatsumsatz):
    if monatsumsatz < 5000:
        gehaltszuschlag = 10
    elif monatsumsatz >= 5000 and monatsumsatz < 10000:
        gehaltszuschlag = 15
    else:
        gehaltszuschlag = 23
    return gehaltszuschlag


bruttogehalt = 0
betriebszugehörigkeit = int(input("Geben Sie bitte ein, wie lange arbeiten Sie schon?: "))
monatsumsatz = int(input("Geben Sie bitte ein, wie hoch ist Ihr Monatsumsatz?: "))
gehalt = bestimmen_gehaltshöhe(betriebszugehörigkeit)
gehaltszuschlag = bestimmen_gehaltszuschlaghöhe(monatsumsatz)
    
bruttogehalt = gehalt/100 * gehaltszuschlag + gehalt

print(f"Ihr Bruttogehalt beträgt : {bruttogehalt}")
      