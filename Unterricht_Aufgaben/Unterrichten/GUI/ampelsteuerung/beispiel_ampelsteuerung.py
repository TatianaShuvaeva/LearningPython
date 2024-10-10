from Unterricht_Aufgaben.Unterrichten.GUI.ampelsteuerung.ampelsteuerung import Ampeln, AutoAmpel, FussgaengerAmpel

autoampel = AutoAmpel()
fussgaengerampel = FussgaengerAmpel()


for i in range(0, len(autoampel.farben)+1):
    print(autoampel.farbe)
    autoampel.umschalten()

print("--------")   
 
for i in range(0, len(fussgaengerampel.farben)+1):
    print(fussgaengerampel.farbe)
    fussgaengerampel.umschalten()
