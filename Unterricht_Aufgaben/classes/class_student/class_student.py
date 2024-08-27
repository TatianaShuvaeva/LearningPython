class Student:
    def __init__(self, vorname, geschlecht, alter, fachrichtung):
        self.__vorname = vorname
        self.geschlecht = geschlecht
        self.__alter = alter
        self.fachrichtung = fachrichtung
        
        
    def hat_geburtstag(self):
        self.__alter += 1
    
    def get_alter(self):
        return self.__alter
        
        
    def weckselt_fachrichtung(self, neu_fachrichtung):
        # if neu_fachrichtung == "Fachrichtung Technik" or neu_fachrichtung == "Fachrichtung Management":
        if neu_fachrichtung in ["Fachrichtung Technik", "Fachrichtung Management", "Design", "Data Analyse", "Technik"]:
            self.fachrichtung = neu_fachrichtung
        else:
            print("Ungültiges Fach")
            
    def __str__(self):
        return (f"Vorname: {self.__vorname:>6}    "
                f" Geschlecht: {self.geschlecht:>6}    "
                f" Alter: {self.__alter:>3}    " 
                f" Fachrichtung: {self.fachrichtung:>6}    ")
