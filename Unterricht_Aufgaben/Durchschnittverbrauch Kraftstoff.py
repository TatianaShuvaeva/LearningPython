# kraftstoffmenge = float(input("Bitte geben Sie die kraftstoffmenge ein: "))
# kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))

# durchschnittverbrauch = (kraftstoffmenge/kilometer) * 100

# print(f"Durchschnittverbrauch:{durchschnittverbrauch} Liter/100 km")

# richtig_eingeben = False
# Versuchen = 1
# kraftstoffmenge = float(input("Bitte geben Sie die Kraftstoffmenge ein: "))
# kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))
# while Versuchen > 0:

#     if kraftstoffmenge > 0:

#         if kilometer > 0:
#             durchschnittverbrauch = round((kraftstoffmenge/kilometer) * 100)
#             print(f"Durchschnittverbrauch: {
#                   durchschnittverbrauch} Liter/100 km")
#             richtig_eingeben = True
#             break
#         else:
#             print(f"Die gefahrene Kilometer sollte > 0 sein")
#             kilometer = float(
#                 input("Bitte geben Sie noch mal die gefahrenen Kilometer ein: "))
#     else:
#         print(f"Die Kraftstoffmenge sollte > 0 sein")
#         kraftstoffmenge = float(
#             input("Bitte geben Sie noch mal die Kraftstoffmenge ein: "))



kraftstoffmenge = 0
kilometer = 0

while kraftstoffmenge <= 0 or kilometer <=0:  # Beginn einer Schleife, die nur durch ein break beendet

    if kraftstoffmenge <= 0:  # Überprüfung, ob die eingegebene Kraftstoffmenge gültig ist
        print("Die Kraftstoffmenge sollte > 0 sein")
        kraftstoffmenge = float(input("Bitte geben Sie die Kraftstoffmenge ein: "))
        
    if kilometer <= 0:  # Überprüfung, ob die eingegebenen Kilometer gültig sind
        print("Die gefahrenen Kilometer sollten > 0 sein")
        kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))
        
        
durchschnittverbrauch = round((kraftstoffmenge/kilometer) * 100)
print(f"Durchschnittverbrauch: {durchschnittverbrauch} Liter/100 km")  
