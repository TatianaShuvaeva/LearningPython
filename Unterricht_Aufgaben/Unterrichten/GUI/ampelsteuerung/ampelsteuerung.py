from abc import ABC, abstractmethod

class Ampeln(ABC):
    
    @abstractmethod
    def umschalten(self):
        pass
    
class AutoAmpel(Ampeln):
    def __init__(self):
        self.farbe = ["rot", "rot-gelb", "gelb","grün"]
    
    def umschalten_AutoAmpel(self):
        
        