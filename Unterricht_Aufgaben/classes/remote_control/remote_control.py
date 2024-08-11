class RemoteControl:
    def __init__(self, anzahl_programme) -> None:
        if anzahl_programme > 10:
            raise Exception("Ungültige Angabe")
        
        self.lautstärke = 0
        self.aktuelles_programm: str = None

        list_programm = ["ARD", "ZDF", "RBB", "RTL", "KiKA", "PHOENIX", "NTV", "PRO7", "KABEL1", "WDR"]
        self.programm = list_programm[:anzahl_programme]       

        self.anzahl = anzahl_programme
                       
    def setProgramName(self, name: str):
        existiert = name in self.programm
        if existiert == False:
            raise Exception("Ungültige Angabe")
           
        self.aktuelles_programm = name
        
    def nextProgram(self):
        unsere_programmliste = self.programm 
     
        index_programm = unsere_programmliste.index(self.aktuelles_programm)
        if index_programm < self.anzahl - 1:
            index_programm += 1
            self.aktuelles_programm = self.programm[index_programm]
        else:
            self.aktuelles_programm = self.programm[0]
    
    
    def plus_lautstärke(self):
        if self.lautstärke >=10:
            return

        self.lautstärke += 1
    

    def minus_lautstärke(self):
        if self.lautstärke <=0:
            return

        self.lautstärke -= 1
    
    def printProgram (self):
        print(self.aktuelles_programm)   
    