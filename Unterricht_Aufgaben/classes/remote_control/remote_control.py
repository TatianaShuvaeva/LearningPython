# Definition der Klasse RemoteControl
class RemoteControl:
    
    # Definition der Konstruktormethode
    def __init__(self, anzahl_programme) -> None:
        if anzahl_programme > 10:
            raise Exception("Ungültige Angabe")
        
        self.__lautstärke = 0
        self.aktuelles_programm: str = None
        
        list_programm = ["ARD", "ZDF", "RBB", "RTL", "KiKA", "PHOENIX", "NTV", "PRO7", "KABEL1", "WDR"]
        self.programm = list_programm[:anzahl_programme]       

        self.anzahl = anzahl_programme
                       
    def setProgramName(self, name: str):
        existiert = name in self.programm
        if existiert == False:
            raise Exception("Es gibt keinen solchen Programmnamen")
           
        self.aktuelles_programm = name
        
    def nextProgram(self):
        index_programm = self.programm.index(self.aktuelles_programm)
        if index_programm < self.anzahl - 1:
            index_programm += 1
            self.aktuelles_programm = self.programm[index_programm]
            return

        self.aktuelles_programm = self.programm[0] 
    
    # Definition der Methode zum Erhöhen der Lautstärke
    def plus_lautstärke(self):
        if self.__lautstärke >=10:
            return

        self.__lautstärke += 1
    
    # Definition der Methode zum Verringern der Lautstärke
    def minus_lautstärke(self):
        if self.__lautstärke <=0:
            return

        self.__lautstärke -= 1
        
    def get_lautstärke(self) -> int:
        return self.__lautstärke
    
    def __str__(self) -> str:
        return (f"Nr: {self.programm.index(self.aktuelles_programm)+1:>2}  "
                f"Name: {self.aktuelles_programm:>6}  "
                f"Lautstärke: {self.__lautstärke:>5}  ")  
    