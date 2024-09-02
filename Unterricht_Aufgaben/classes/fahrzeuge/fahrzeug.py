class Fahrzeug:
    def __init__(self, marke: str, baujahr: int, km_stand: float, farbe: str):
        if km_stand < 0:
            raise ValueError("Kilometerstand muss positiv sein.")

        self.__marke = marke
        self.__baujahr = baujahr
        self.__km_stand = km_stand
        self.__farbe = farbe

    def get_km_stand(self) -> float:
        return self.__km_stand

    def set_km_stand(self, neu_km_stand: float):
        if neu_km_stand < self.__km_stand:
            raise ValueError("Neuer Kilometerstand muss größer oder gleich alter sein.")

        self.__km_stand = neu_km_stand

    def get_farbe(self) -> str:
        return self.__farbe

    def __str__(self):
        return f"Fahrzeug {self.__marke}: Baujahr - {self.__baujahr}, km Stand - {self.__km_stand}, Farbe - {self.__farbe}"
