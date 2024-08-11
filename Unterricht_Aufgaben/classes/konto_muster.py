# Definition der Klasse Konto
class Konto:
    def __init__(self, kontonummer, inhaber, saldo):
        self.ktoNr = kontonummer
        self.inhaber = inhaber
        self.ktoStand = saldo

    def einzahlen(self, betrag):
        if betrag <= 0:
            print("Ungültige Angabe")
        else:
            self.ktoStand += betrag

    def auszahlen(self, betrag):
        if self.ktoStand < betrag:
            print("Konto kann nicht überzogen werden")
        else:
            self.ktoStand -= betrag

konto_hans = Konto("987654", "Hans", 100)
konto_karl = Konto("123456", "Karl", 500)

print(konto_karl.ktoStand)
konto_karl.einzahlen(200)
konto_karl.einzahlen(400)
print(konto_karl.ktoStand)

konto_karl.auszahlen(7000)
print(konto_karl.ktoStand)


konto_hans.einzahlen(-50)

einzahlungsbetrag = int(input("Einzahlungsbetrag:"))
konto_hans.einzahlen(einzahlungsbetrag)
print(konto_hans.ktoStand)