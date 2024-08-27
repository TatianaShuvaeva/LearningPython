# Klasse RemoteControl definieren
class RemoteControl:
    # Konstruktor, dem die maximale Anzahl an Programmspeicherplätzen
    # zur Initialisierung übergeben wird
    def __init__(self, num_programs):
        self.__programs = []
        # Initialisierung der Programmspeicherplätze
        for i in range(0, num_programs):
            self.__programs += ["Prog " + str(i+1)]
        self.__current_program_number = 0
        self.__volume = 0
        
    # Methode zur Benennung des aktuellen Programms
    def setProgramName(self, name):
        self.__programs[self.__current_program_number] = name
        
    # Methode für den Wechsel zum nächsten Programm
    def nextProgram(self):
    # Gehe zum nächsten Programm, wenn noch nicht das Ende der Liste erreicht ist
        if self.__current_program_number < len(self.__programs) - 1:
            self.__current_program_number += 1
        # sonst beginne wieder beim ersten Programm
        else:
            self.__current_program_number = 0
            
        # Definition der Methode zum Erhöhen der Lautstärke
    def plus(self):
        if self.__volume >= 10:
            print("Lautstärke lässt sich nicht weiter erhöhen")
        else:
            self.__volume += 1

    # Definition der Methode zum Verringern der Lautstärke
    def minus(self):
        if self.__volume > 0:
            self.__volume -= 1
        else:
            print("Lautstärke ist bereits 0")
    
    # Methode zum Ausgeben des aktuellen Programms
    # mit Nummer, Name und aktueller Lautstärke

    def __str__ (self):
        return (f"Nr {str(self.__current_program_number):>2} "
                 f"Name {str(self.__programs[self.__current_program_number]):>6} "
                 f"Lautstärke {str(self.__volume):>2} ")
