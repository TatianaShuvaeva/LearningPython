from remote_control import RemoteControl

p1 =  RemoteControl(5)
print(p1.programm)
print(p1.aktuelles_programm)

p1.setProgramName("KiKA")
print(p1.aktuelles_programm)
p1.nextProgram()
print(p1.aktuelles_programm)