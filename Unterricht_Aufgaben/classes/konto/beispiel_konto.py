from konto import Konto

# konto1 = Konto("Schmidt", 12345678911, 250.67, 150)
# konto2 = Konto("schmidt", 12345678911, 250.67, 150)
# konto3 = Konto("Henkel", 12345678911, 250.67, 150)
# print(konto1==konto2)
# print(konto1==konto3)

konto1 = Konto("Schmidt", 12345678911, 200.67, 150)
konto2 = Konto("schmidt", 12345678911, 250.67, 150)
konto1.umsatz = 50
konto2.umsatz = 100
print(konto1==konto2)
