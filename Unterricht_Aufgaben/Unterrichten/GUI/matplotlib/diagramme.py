import matplotlib.pyplot as plt

# Y Werte
plt.plot([1, 2, 3, 4, 5, 6], [0, 2, 4, 8, 10, 11], label="Blau")
x_werte = [2, 3, 4, 5, 6]
y_werte = [3, 4, 5, 6, 7]
plt.plot(x_werte, y_werte, label="Linie")
plt.legend(loc="lower left")
# Raster
plt.grid(True)
plt.show()
