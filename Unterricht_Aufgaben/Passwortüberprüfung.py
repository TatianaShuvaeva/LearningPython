import datetime

benutzername_aus_db = 'tatiana'
passwort_aus_db = 'test'
versuchen = 0
anmeldung_erlaubt = False
benutzer_gesperrt = True
# benutzer_gesperrt = False
# sperrdatum_utc = None
sperrdatum_utc = datetime.datetime(2024, 5, 5, 19, 10, 51, 0)

while versuchen < 3:
    benutzername = str(input("Bitte geben Sie den Benutzername ein: "))
    passwort = str(input("Bitte geben Sie das Passwort ein: "))
    if benutzername == benutzername_aus_db and passwort ==passwort_aus_db:
       
        if  benutzer_gesperrt is True:
            differenz = datetime.datetime.today() - sperrdatum_utc
            differenz_in_stunden = differenz.days * 24 + differenz.seconds / 60 / 60
            if differenz_in_stunden < 24:
                print("Seit der Sperrung sind weniger als 24 Stunden vergangen")
                # break
            else:
                benutzer_gesperrt = False
                anmeldung_erlaubt = True
                sperrdatum_utc = None
                # break
        else:
            anmeldung_erlaubt = True
            # break
        
        break
    
    else:
        versuchen += 1
        print(("Die Anmeldung ist fehlgeschlagen"))
    
if anmeldung_erlaubt is True:
    print("Anmeldung erlaubt")
elif benutzer_gesperrt is False:
    benutzer_gesperrt = True
    sperrdatum_utc = datetime.datetime.today()
    print(f"Ihr Konto ist gesperrt {sperrdatum_utc}")
        