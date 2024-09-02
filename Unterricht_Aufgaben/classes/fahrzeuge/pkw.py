from fahrzeug import Fahrzeug


class PKW(Fahrzeug):
    def __init__(self, marke: str, baujahr: int, km_stand: float, farbe: str, kofferraumvolumen: int):
        super().__init__(marke, baujahr, km_stand, farbe)
        
        if kofferraumvolumen < 0:
            raise ValueError("Kofferraumvolumen muss positiv sein.")
        
        self.__kofferraumvolumen = kofferraumvolumen

    def __str__(self):
        return f"{super().__str__()}, Kofferraumvolumen - {self.__kofferraumvolumen}"
