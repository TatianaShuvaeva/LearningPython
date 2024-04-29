brustumfang = float(input("Bitte geben Sie den Brustumfang Ihrer Katze in Zentimetern ein: "))
beinlänge = float(input("Bitte geben Sie die Beinlänge Ihrer Katze in Zentimetern ein: "))

# Berechnung des FBMI gemäß den angegebenen Schritten
fbmi = round(((brustumfang / 0.7062) - beinlänge) / 0.9156 - beinlänge)

print("Der FBMI Ihrer Katze beträgt:", fbmi)

# Empfehlungen basierend auf dem FBMI
if fbmi < 15:
    print("Ihre Katze hat einen FBMI unter 15. Sie sollte möglicherweise mehr fressen.")
elif fbmi >= 15 and fbmi <= 29.9:
    print("Ihre Katze hat einen gesunden FBMI. Weiter so!")
else:
    print("Ihre Katze hat einen FBMI über 30. Vielleicht sollte sie weniger Kalorien zu sich nehmen.")

