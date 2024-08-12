from remote_control import RemoteControl

# Lautstärkeprüfung
rc1 = RemoteControl(2)

assert rc1.lautstärke == 0, 'Lautstärke soll man 0 sein'

rc1.plus_lautstärke()
assert rc1.lautstärke == 1, 'Lautstärke soll man 1 sein'
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
rc1.plus_lautstärke()
assert rc1.lautstärke == 10, '10 - max Lautstärke'

rc2 = RemoteControl(5)
rc2.minus_lautstärke()
assert rc2.lautstärke == 0, 'Lautstärke soll man 0 sein'

rc2.plus_lautstärke()
rc2.plus_lautstärke()
rc2.minus_lautstärke()
assert rc2.lautstärke == 1, 'Lautstärke soll man 1 sein'

# Prüfung des aktuellen Programms
rc3 = RemoteControl(5)
assert rc3.aktuelles_programm == None, 'Soll None sein'

rc4 = RemoteControl(5)
rc4.setProgramName("KiKA")
assert rc4.aktuelles_programm == "KiKA", 'Soll "KiKA" sein'
rc4.nextProgram()
assert rc4.aktuelles_programm == "ARD", 'Soll "ARD" sein'
rc4.nextProgram()
assert rc4.aktuelles_programm == "ZDF", 'Soll "ZDF" sein'
rc4.printProgram()
