# Definition der Klasse Person
class Person:
    # Definition der Konstruktor-Methode
    def __init__(self, p_nachname, p_vorname, alter, wohnort):
        self.nachname = p_nachname
        self.vorname = p_vorname
        self.alter = alter
        self.wohnort = wohnort

    def name_aendern(self, neuer_name):
        self.nachname = neuer_name

    def umziehen(self, neuer_wohnort):
        self.wohnort = neuer_wohnort

# Instanziierung eines Objektes der Klasse Person


p1 = Person("Lehman", "Karl", 42, "Berlin")
p2 = Person("Schmidt", "Anna", 24, "Dresden")

# print(type(p1))
# print(p1.vorname, p1.nachname)

p2.name_aendern("Henkel")
print(f"{p2.vorname} hat ihren Nachnamen geändert und heißt nun {p2.vorname} {p2.nachname}")

p1.umzihen("Köln")
print(f"{p1.vorname} {p1.nachname} ist umgezogen und wohnt jetzt in {p1.wohnort}")
