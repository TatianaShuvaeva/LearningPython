from konto import Konto

# konto1 = Konto("Schmidt", 12345678911, 5000.67, 200)
# konto2 = Konto("Müller", 12345678910, 5000.67, 200)
# konto3 = Konto("Henkel", 12345678912, 3000.34, 150)

# konto1.umsatz = 50

# print(konto1 == konto2)
# print(konto1 == konto3)

konto1 = Konto("Schmidt", 12345678911, 200.67, 200)
konto2 = Konto("Henkel", 12345678912, 250.67, 150)
konto1.umsatz = 100
konto2.umsatz = 50

assert konto1 == konto2