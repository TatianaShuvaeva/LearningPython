# Definition der Klasse Konto

class Konto:
    def __init__(self, kontonummer):
    self.ktoNr = kontonummer
    self.inhaber = inhaber
    self.ktoStand = saldo
konto_hans = Konto("987654", "Hans", 100)

print(type(konto_hans))
print(konto_hans.ktoNr)


konto_karl = Konto("123456", "Karl", 500)
print(konto_karl.ktoNr, konto_karl.ktoStand)