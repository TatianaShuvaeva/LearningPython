# Zufallgenerator
import random
random.seed()

# Anzahl Aufgaben
anzahl = -1
while anzahl < 1 or anzahl > 10:
    try:
        anzahl = int(input("Wie viele Aufgaben (1 bis 50):  "))
        
    except:
        continue

# Anzahl richtige Ergebnisse
richtig = 0

# Schleife mit gewünschter Anzahl an Aufgaben
for aufgabe in range(1, anzahl + 1):
    # Operatorauswahl
    opzahl = random.randint(1,4)
    
    # Operandenauswahl
    if opzahl == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = "+"
        c = a + b
    elif opzahl == 2:
        a = random.randint(10, 20)
        b = random.randint(1, 10)
        op = "-"
        c = a - b
    # elif opzahl == 3:
    #     a = random.randint(1, 10)
    #     b = random.randint(1, 10)
    #     op = "*"
    #     c = a * b
    # # Sonderfall Division
    # elif opzahl == 4:
    #     a = random.randint(1, 10)
    #     b = random.randint(1, 10)
    #     op = "/"
    #     c = round(a / b)
    # Aufgabenstellung
    print(f"Aufgabe {aufgabe} von {anzahl}: {a} {op} {b}")

    # Schleige mit 3 Versuchen
    for versuch in range(1, 4):
        # Eingabe
        try:
            zahl = int(input("Bitte Lösungvorschlag eingeben:  "))
            
        except:
            # Umwandlung war nicht erfolgreich
            print("Sie haben keine ganze Zahl eingegeben")
            # Schleife unmittelbar forsetzen
            continue
        # Kommentar
        if zahl == c:
            print(zahl, "ist richtig")
            richtig = richtig + 1
            break
        else:
            print(zahl, "ist falsch")

    # Richtiges Ergebnis der Aufgabe
    print("Ergebnis: ", c)

# Anzahl richtige Ergebnisse
print(f"Richtig: {richtig} von {anzahl}")
