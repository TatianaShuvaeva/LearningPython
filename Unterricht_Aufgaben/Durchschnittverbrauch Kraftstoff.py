# kraftstoffmenge = float(input("Bitte geben Sie die kraftstoffmenge ein: "))
# kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))

# durchschnittverbrauch = (kraftstoffmenge/kilometer) * 100

# print(f"Durchschnittverbrauch:{durchschnittverbrauch} Liter/100 km")


kraftstoffmenge = float(input("Bitte geben Sie die kraftstoffmenge ein: "))
if kraftstoffmenge <= 0:
    print(f"Ihre Zahl: {kraftstoffmenge} sollte eine positive Zahl sein")
    kraftstoffmenge = float(input("Bitte geben Sie die kraftstoffmenge ein: "))
    
kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))
if kilometer <= 0:
    print(f"Ihre Zahl: {kilometer} sollte eine positive Zahl sein")
    kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))
    
durchschnittverbrauch = (kraftstoffmenge/kilometer) * 100
print(f"Durchschnittverbrauch:{durchschnittverbrauch} Liter/100 km")
