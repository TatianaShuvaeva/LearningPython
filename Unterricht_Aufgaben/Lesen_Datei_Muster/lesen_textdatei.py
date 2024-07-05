try:
    eingabe_datei = open("test.txt", "r")
    for zeile in eingabe_datei:
        print(zeile, end = "")
    eingabe_datei.close()
except FileNotFoundError as err:
    print("Dateizugriffsfehler", err)
    exit(99)
except:
    print("sonstige Dateifehler")
    exit(100)