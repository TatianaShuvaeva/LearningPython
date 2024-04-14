Zahl = float(input("Zahl eingeben: "))  # Nimmt eine Zahl als Eingabe
Einheit = input("Kb/Mb/Gb: ").lower()   # Nimmt die Einheit als Eingabe und wandelt sie in Kleinbuchstaben um

# Führt die Konvertierung entsprechend der Einheit durch
if Einheit == "kb":
    print(f"{Zahl / 1000} Mb")  # Konvertiert Kb in Mb
elif Einheit == "mb":
    print(f"{Zahl / 1000} Gb")  # Konvertiert Mb in Gb
elif Einheit == "gb":
    print(f"{Zahl / 1000} Tb")  # Konvertiert Gb in Tb
else:
    print("Ungültige Einheit. Bitte geben Sie Kb, Mb oder Gb ein.")
