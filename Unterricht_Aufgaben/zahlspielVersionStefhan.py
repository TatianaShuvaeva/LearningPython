print("Errate die Zahl zwischen 1 und 100")
Versuchemax = 10
richtig_erraten = False
while Versuchemax > 0:
    DeineZahl = int(input("Gib deine Zahl ein: "))
    if (DeineZahl >= 1) and (DeineZahl <= 100):
        x = 15
        if x < DeineZahl:
            print(f"Deine geratene Zahl: {DeineZahl} ist größer als x")
        elif x > DeineZahl:
            print(f"Deine geratene Zahl ist: {DeineZahl} ist kleiner als x")
        else:
            print(f"Deine geratene Zahl ist: {DeineZahl} ist korrekt")
            richtig_erraten = True
            break

        Versuchemax -= 1
    else:
        print(f"Deine Zahl: {
              DeineZahl} liegt nicht im Bereich! Errate bitte die Zahl zwischen 1 und 100")

if richtig_erraten == False:
    print(f"Schade! Leider hatte mehr als die maximale Anzahl der Versuchen :( ")
