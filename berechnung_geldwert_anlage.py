anlagebetrag = int(input("Geben Sie bitte den Anlagebetrag ein: "))
anzahl_anlagejahre = int(input("Geben Sie bitte den Anzahl der Anlagejahre ein: "))
zinssatz = int(input("Geben Sie bitte den Zinssatz pro Jahr in % ein: "))
laufzeit = 0
wert_anlage = anlagebetrag
while laufzeit < anzahl_anlagejahre:
    wert_anlage = round(wert_anlage/100*zinssatz+wert_anlage,2)
    laufzeit += 1
print(f'Wert der Anlage nach Ende der Laufzeit - {wert_anlage} Euro')