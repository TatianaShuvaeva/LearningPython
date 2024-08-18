# Definition der Klasse RemoteControl
class RemoteControl:
    # Definition der Konstruktormethode
    def __init__(self, num_programs):
        self.volume = 5

        self.programs = []
        for i in range(0, num_programs):
            self.programs += ["Prog"+str(i+1)]

        self.curr_program_number = 0


        # Definition der Methode zum Erhöhen der Lautstärke
    def plus(self):
        if self.volume >= 10:
            print("Lautstärke lässt sich nicht weiter erhöhen")
        else:
            self.volume += 1

    # Definition der Methode zum Verringern der Lautstärke
    def minus(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Lautstärke ist bereits 0")

    def setProgramName(self, name):
        self.programs[self.curr_program_number] = name

    def nextProgram(self):
        self.curr_program_number += 1
    