def rechnen_bmi():
    koerpergewicht = float(input("Bitte geben Sie ihr Körpergewicht in Kilogramm ein: "))
 
    while koerpergewicht <= 0: #Falsche Variable im Struktogramm (Körpergröße)
        print("Bitte einen gültigen Wert eingeben")
        koerpergewicht = float(input("Bitte geben sie ihr Körpergewicht in Kilogramm ein: "))
 
    groesse = float(input("Bitte geben Sie Ihre Größe in meter ein: "))
 
    while groesse <= 0:
        print("Bitte einen gültigen Wert eingeben")
        groesse = float(input("Bitte geben Sie Ihre Größe in meter ein: "))
 
 
    bmi = round(koerpergewicht / groesse * groesse, 2) #Die Formel hat einen Fehler. Die korrekte Formel lautet: koerpergewicht / (groesse * groesse)
 
    if bmi <= 18.4:
        print(f"Ihr BMI Wert beträgt {bmi} sie sind untergewichtig")
 
    elif bmi <= 24.9:
        print(f"Ihr BMI Wert beträgt {bmi} sie sind normal Gewicht")
 
    elif bmi <= 39.9:
        print(f"Ihr BMI Wert beträgt {bmi}. Sie sind übergewichtig")
 
    else: print(f"Ihr BMI Wert beträgt {bmi}. Sie leiden an Adipositas")

try:
    rechnen_bmi()
 
except: #Catch funktion gibt es nicht in Phython, wir haben except benutzt.
    print("Keine gültige Eingabe! Bitte einen korrekten Wert eintragen")
 
#Da wir except benutzt haben, können wir finally weglassen