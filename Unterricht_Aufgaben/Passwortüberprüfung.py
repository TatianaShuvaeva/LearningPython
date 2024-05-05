benutzername_aus_db = 'tatiana'
passwort_aus_db = 'test'
versuchen = 0
benutzername_und_passwort_richtig = False
while versuchen < 3:
    benutzername = str(input("Bitte geben Sie den Benutzername ein: "))
    passwort = str(input("Bitte geben Sie das Passwort ein: "))
    if benutzername == benutzername_aus_db and passwort ==passwort_aus_db:
        benutzername_und_passwort_richtig = True
        break
    else:
        versuchen += 1
        print(("Die Anmeldung ist fehlgeschlagen"))
    
if benutzername_und_passwort_richtig is True:
    print("Anmeldung erlaubt")
        