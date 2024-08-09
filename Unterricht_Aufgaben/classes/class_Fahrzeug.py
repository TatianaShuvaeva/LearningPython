# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, h, t, f,g = 0):
        self.hersteller = h
        self.typ = t
        self.farbe = f
        self.geschwindigkeit = g
    def gasgeben(self, wert):
        self.geschwindigkeit += wert
    def stop (self):
        self.geschwindigkeit = 0


f1 = Fahrzeug("VW", "Golf", "rot")
print(f"Hersteller: {f1.hersteller} - Typ{f1.typ} hat die Farbe {f1.farbe} und fährt {f1.geschwindigkeit} km/h")

f2 = Fahrzeug("Ferrari", "SF90", "rot", 50)
print(f"Hersteller: {f1.hersteller} - Typ{f1.typ} hat die Farbe {f1.farbe} und fährt {f1.geschwindigkeit} km/h")

f1.gasgeben(60)
print(f"Hersteller: {f1.hersteller} - Typ{f1.typ} hat die Farbe {f1.farbe} und fährt {f1.geschwindigkeit} km/h")
f1.gasgeben(60)
print(f"Hersteller: {f1.hersteller} - Typ{f1.typ} hat die Farbe {f1.farbe} und fährt {f1.geschwindigkeit} km/h")
f1.stop()
print(f"Hersteller: {f1.hersteller} - Typ{f1.typ} hat die Farbe {f1.farbe} und fährt {f1.geschwindigkeit} km/h")