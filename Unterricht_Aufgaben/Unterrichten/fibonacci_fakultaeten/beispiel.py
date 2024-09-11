from modul import *

anzahl_studenten_uni = 1000
# anzahl_studenten_uni = -10
# anzahl_studenten_uni = "10"
#anzahl_studenten_uni = 10.1
liste_fakultaeten, studenten_fakultaeten = erstellen_fakultaeten(anzahl_studenten_uni)

print(f"An der Uni wurden Fakultäten {liste_fakultaeten} mit einer Gesamtzahl von Studenten {studenten_fakultaeten} geschaffen")