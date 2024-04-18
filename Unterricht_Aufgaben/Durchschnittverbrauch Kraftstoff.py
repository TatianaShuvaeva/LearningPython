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


richtig_eingeben = False
Versuchen = 1

kraftstoffmenge = float(input("Bitte geben Sie die Kraftstoffmenge ein: "))
kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))

while not richtig_eingeben:  # Beginn einer Schleife, die nur durch ein break beendet

    if kraftstoffmenge > 0:  # Überprüfung, ob die eingegebene Kraftstoffmenge gültig ist

        if kilometer > 0:  # Überprüfung, ob die eingegebenen Kilometer gültig sind

            durchschnittverbrauch = round((kraftstoffmenge/kilometer) * 100)
            print(f"Durchschnittverbrauch: {durchschnittverbrauch} Liter/100 km")
                  

            richtig_eingeben = True   # Setzen der Flagge für korrekte Eingabe auf True
            break  # Beenden der Schleife

        else:
            print("Die gefahrenen Kilometer sollten > 0 sein")
            kilometer = float(
                input("Bitte geben Sie die gefahrenen Kilometer ein: "))

    else:

        print("Die Kraftstoffmenge sollte > 0 sein")
        kraftstoffmenge = float(
            input("Bitte geben Sie die Kraftstoffmenge ein: "))
