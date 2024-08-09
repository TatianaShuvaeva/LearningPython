# Definition der Klasse Person
class Person:
   # Definition der Konstruktor-Methode
   def __init__(self, p_nachname, p_vorname):
        self.nachname = p_nachname
        self.vorname = p_vorname

# Instanziierung eines Objektes der Klasse Person

p1 = Person("Lehman", "Karl")


p2 = Person("Schmidt", "Anna")

print(type(p1))
print(p1.vorname, p1.nachname)