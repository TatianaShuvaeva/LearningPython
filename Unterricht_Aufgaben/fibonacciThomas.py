# definieren einer Funktion mit dem Namen 'fibonacci', die einen Parameter 'n' akzeptiert
def fibonacci(n):
    # es wird überprüft ob 'n' kleiner oder gleich 0 ist, dies ist eine Bedingung für die Rekursion,
    # Rekursion bedeutet, dass sich die Fkt. selbst mit neuen Argumenen aufruft
    # hier muss das Null-Problem bzw. negative Zahlen behandelt werden
    if n <= 0:
         # wenn 'n' kleiner gleich 0 ist dann gib die Funktion '0' zurück
        return 0
    # hier wird geprüft ob n gleich 1 ist
    elif n == 1:
        # wenn 'n' gleich 1 ist gib der Funktion 1 zurück, hier sind keine Rekursionen notwendig, da der Wert n gleich 1 dem Wert der Fibonacci-Sequenz entpricht
        return 1
    else:
        # das ist der rekursive Teil der Funktion, die Funktion wird zweimal aufgerufen mit 'n-1' und 'n-2' als Argumente
        # es geht darum den Vorgänger und den Vorvorgänger zu summieren um einen Fibonacci-Wert zu erhalten
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(19))