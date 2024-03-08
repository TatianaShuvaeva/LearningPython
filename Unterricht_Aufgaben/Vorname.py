vorname = str(input('Bitte Ihren Vorname eingeben '))
klassische_namen = ["Anna", "Hans", "Marie", "Klaus", "Christine", "Peter", "Susanne",
                    "Michael", "Elisabeth", "Andreas", "Sabine", "Thomas", "Monika", "Stefan", "Petra"]
if vorname in klassische_namen:
    print(f"Herzlichen Glückwunsch {
          vorname}, Sie haben die Klausur bestanden.")
else:
    print(f"Es tut uns leid {vorname}, Sie haben die Klausur durchgefallen :(")
