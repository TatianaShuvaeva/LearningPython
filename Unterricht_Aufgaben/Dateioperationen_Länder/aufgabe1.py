from datei_einlesen import get_länder

try:
    print(get_länder())
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except Exception as err:
    print("Sonstige Dateifehler", err)
    exit(100)