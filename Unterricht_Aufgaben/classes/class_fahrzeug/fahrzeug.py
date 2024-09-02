class Fahrzeug:
    def __init__(self, marke: str, baujahr: int, km_stand: float, farbe: str):
        self.__marke = marke
        self.__baujahr = baujahr
        self.__km_stand = km_stand
        self.__farbe = farbe

    def __str__(self):
        return f"Fahrzeug {self.__marke}: Baujahr - {self.__baujahr}, km Stand - {self.__km_stand}, Farbe - {self.__farbe}"
