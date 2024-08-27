# Einbinden der Klassendefinition
from RemoteControl import RemoteControl

# Klasse RemoteControl instanziieren - mit 5 Programmplätzen
rc = RemoteControl(5)
# aktuellen Programmplatz: Programmname setzen
rc.setProgramName("ARD")
# aktuellen Programmplatz: Programmnummer und Programmname ausgeben
print(rc)
# gehe 1 Sender weiter
rc.nextProgram()
# aktuellen Programmplatz: Programmnummer und Programmname ausgeben
print(rc)
# aktuellen Programmplatz: Programmname setzen
rc.setProgramName("ZDF")
# aktuellen Programmplatz: Programmnummer und Programmname ausgeben
print(rc)
# rc.__program[3] = "RTL"
# führt zu AttributeError: 'RemoteControl' object has no attribute '__program'
rc.plus()
rc.plus()
# aktuellen Programmplatz: Programmnummer und Programmname ausgeben
print(rc)
rc.minus()
print(rc)