spannung = 0
strom = 0

while spannung <= 0 or strom <=0:  # Beginn einer Schleife

    if spannung <= 0:  # Überprüfung, ob die elektrische Spannung gültig ist
        print("Die elektrische Spannung sollte > 0 sein")
        spannung = float(input("Bitte geben Sie die elektrische Spannung ein: "))
        
    if strom <= 0:  # Überprüfung, ob die elektrische Stromstärker gültig sind
        print("Die elektrische Stromstärke sollten > 0 sein")
        strom = float(input("Bitte geben Sie die elektrische Stromstärke ein: "))
        
        
widerstand = round(spannung / strom)
print(f"Der elektrische Widerstand beträgt {widerstand} Ohm.")  


