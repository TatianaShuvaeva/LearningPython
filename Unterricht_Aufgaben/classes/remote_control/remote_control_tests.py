from remote_control import RemoteControl

# Lautstärkeprüfung
p1 = RemoteControl(2)

assert p1.lautstärke == 0, 'Lautstärke soll man 0 sein'

p1.plus_lautstärke()
assert p1.lautstärke == 1, 'Lautstärke soll man 1 sein'
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
p1.plus_lautstärke()
assert p1.lautstärke == 10, '10 - max Lautstärke'

p2 = RemoteControl(5)
p2.minus_lautstärke()
assert p2.lautstärke == 0, 'Lautstärke soll man 0 sein'

p2.plus_lautstärke()
p2.plus_lautstärke()
p2.minus_lautstärke()
assert p2.lautstärke == 1, 'Lautstärke soll man 1 sein'

# Prüfung des aktuellen Programms
p3 = RemoteControl(5)
assert p3.aktuelles_programm == None, 'Soll None sein'

p4 = RemoteControl(5)
p4.setProgramName("KiKA")
assert p4.aktuelles_programm == "KiKA", 'Soll "KiKA" sein'
p4.nextProgram()
assert p4.aktuelles_programm == "ARD", 'Soll "ARD" sein'
p4.nextProgram()
assert p4.aktuelles_programm == "ZDF", 'Soll "ZDF" sein'
p4.printProgram()
