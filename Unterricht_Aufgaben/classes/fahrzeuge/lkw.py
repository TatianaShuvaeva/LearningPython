from fahrzeug import Fahrzeug


class LKW(Fahrzeug):
    def __init__(self, marke: str, baujahr: int, km_stand: float, farbe: str, gewichtklasse: float):
        super().__init__(marke, baujahr, km_stand, farbe)
        
        if gewichtklasse < 0:
            raise ValueError("Gewichtklasse muss positiv sein.")
        
        self.__gewichtklasse = gewichtklasse

    def __str__(self):
        return f"{super().__str__()}, Gewichtklasse - {self.__gewichtklasse}t"
