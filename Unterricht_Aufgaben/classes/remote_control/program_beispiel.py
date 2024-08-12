from remote_control import RemoteControl

#Instanziierung
rc1 =  RemoteControl(5)
print(rc1.programm)
print(rc1.aktuelles_programm)

rc1.setProgramName("KiKA")
print(rc1.aktuelles_programm)
rc1.nextProgram()
print(rc1.aktuelles_programm)