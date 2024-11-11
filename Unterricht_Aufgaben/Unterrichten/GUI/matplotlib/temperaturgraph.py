import matplotlib.pyplot as plt

tage = ["Freitag", "Samstag", "Sonntag", "Montag", "Dienstag"]
temperaturen = [17.5, 17, 18, 16, 15]


plt.plot(tage, temperaturen, label="Linie")
plt.xlabel("Tag")
plt.ylabel("Temperatur (C)")
plt.legend(loc="lower left")
plt.title("Temperaturen der letzten 5 Tage")

# Raster
plt.grid(True)
plt.show()
