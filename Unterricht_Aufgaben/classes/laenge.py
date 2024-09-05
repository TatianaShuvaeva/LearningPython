# Operatorüberladung

class Laenge:
    umrechnung = {"m": 1,
                  "dm": 0.1,
                  "cm": 0.01,
                  "mm": 0.001,
                  "km": 1000}

    def __init__(self, wert, einheit):
        self.zahlenwert = wert
        self.einheit = einheit

    def __str__(self):
        return f"{self.zahlenwert} {self.einheit}"

    def __add__(self, other):
        z1 = self.zahlenwert * Laenge.umrechnung[self.einheit]
        z2 = other.zahlenwert * Laenge.umrechnung[other.einheit]
        z = z1 + z2
        z = round(z / Laenge.umrechnung[self.einheit], 3)
        return Laenge(z, self.einheit)

    def __sub__(self, other):
        z1 = self.zahlenwert * Laenge.umrechnung[self.einheit]
        z2 = other.zahlenwert * Laenge.umrechnung[other.einheit]
        z = z1 - z2
        z = round(z / Laenge.umrechnung[self.einheit], 3)
        return Laenge(z, self.einheit)

    def __eq__(self, other) -> bool:
        z1 = self.zahlenwert * Laenge.umrechnung[self.einheit]
        z2 = other.zahlenwert * Laenge.umrechnung[other.einheit]
        return z1 == z2


s1 = Laenge(5, "m")
s2 = Laenge(2, "km")
s = s1 + s2
print(s)
s3 = Laenge(90, "cm")
s4 = Laenge(1, "m")

print(s)
if s3 == s4:
    print("ja", s3, s4)
else:
    print("nein", s3, s4)
print(Laenge(5000, "m") == Laenge(5, "km"))
