#  Aufgabe 1

# def zahl_einlesen():
#     # return int(zahl)
#     print(f"Ihre Zahl: {int(zahl)}")
    
# zahl = float(input("Geben Sie bitte eine Zahl ein: "))
# zahl_einlesen()


#  Aufgabe 2

# def celsius_zu_fahrenheit():
#     fahrenheit = zahl * 9/5+32
#     print(f"Eingegebene Temperatur {round(zahl,1)}°C entspricht {round(fahrenheit, 1)}°F")

# zahl = float(input("Geben Sie bitte die Temperatur in Celsius ein:  "))
# celsius_zu_fahrenheit()


#  Aufgabe 3

# def fahrenheit_zu_celsius():
#     celsius = (zahl-32) * 5/9
#     print(f"Eingegebene Temperatur {round(zahl, 1)}°F entspricht {round(celsius,1)}°C")

# zahl = float(input("Bitte die Temperatur in Fahrenheit eingeben: "))
# fahrenheit_zu_celsius()


#  Aufgabe 4

# def modus_einlesen():
#     # return modus
#     print(f"Sie haben eingegeben {modus}")

# modus = str(input("Geben Sie bitte 'F nach C' - wenn Sie die Temperatur in Celsius umrechnen möchten oder 'C nach F' - wenn Sie die Temperatur in Fahrenheit umrechnen möchten oder: ").lower())
# modus_einlesen()


#  Aufgabe 5  

def zahl_einlesen():
    return int(zahl) 

def modus_einlesen() -> str:
    benutzer_input = input("Geben Sie bitte 'F nach C' - wenn Sie die Temperatur in Celsius umrechnen möchten oder 'C nach F' - wenn Sie die Temperatur in Fahrenheit umrechnen möchten oder: ")
    modus = benutzer_input.lower()
    return modus


def f_nach_c(zahl: float) -> float:
    ergebnis = (zahl-32) * 5/9
    return ergebnis

def hauptschleife(modus: str, zahl: float):
    if modus == 'f nach c':
        print(f"Eingegebene Temperatur {int(zahl)}°F entspricht {f_nach_c(zahl)}°C")
    elif modus == 'c nach f': 
        print(f"Eingegebene Temperatur {int(zahl)}°C entspricht {c_nach_f(zahl)}°F")
    else:
        print(f"Sie haben falsche Daten {modus} und {zahl} eingegeben. Versuchen Sie es noch einmal")

def c_nach_f(zahl: float) -> float:
    return zahl * 9/5+32


modus = modus_einlesen()
zahl = float(input("Bitte die Temperatur eingeben: "))
hauptschleife(modus, zahl)


#  Aufgabe 6

# def zahl_einlesen():
#     return int(zahl) 

# def modus_einlesen():
#     return modus

# def hauptschleife(modus_einlesen):
#     if modus_einlesen() == 'f nach c':
#         print(f"Eingegebene Temperatur {int(zahl)}°F entspricht {int((zahl-32) * 5/9)}°C")
#     elif modus_einlesen() == 'c nach f': 
#         print(f"Eingegebene Temperatur {int(zahl)}°C entspricht {int(zahl * 9/5+32)}°F")
#     else:
#         print(f"Sie haben falsche Daten {modus} und {zahl} eingegeben. Versuchen Sie es noch einmal")


# modus = str(input("Geben Sie bitte 'F nach C' - wenn Sie die Temperatur in Celsius umrechnen möchten oder 'C nach F' - wenn Sie die Temperatur in Fahrenheit umrechnen möchten oder: ").lower())
# zahl = float(input("Bitte die Temperatur eingeben: "))
# zahl_n = int(input("Geben Sie bitte die Zahl_n ein, die die in Aufgabe 5 beschriebene Aufgabe n mal ausführen soll: "))
# count = 0

# while count < zahl_n:
#     hauptschleife(modus_einlesen)
#     count += 1