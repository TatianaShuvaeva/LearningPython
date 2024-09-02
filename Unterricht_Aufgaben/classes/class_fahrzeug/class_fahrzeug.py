class Fahrzeug:
    def __init__(self, m, b, kms,f):
        self._marke = m
        self._baujahr = b
        self._km_stand = kms
        self._farbe = f
    
    def __str__(self):
        return f"Fahrzeug {self._marke}: Baujahr - {self._baujahr}, km Stand - {self._km_stand}, Farbe - {self._farbe}"
        
class PKW(Fahrzeug):
    def __init__(self, m,b,kms, f, k):
        super().__init__(m,b,kms,f)
        self._kofferraumvolumen = k
    def get_kofferraumvolumen(self):
        return self._kofferraumvolumen

    def __str__(self):
        return f"Fahrzeug {self._marke}: Baujahr - {self._baujahr}, km Stand - {self._km_stand}, Farbe - {self._farbe}, Kofferraumvolumen - {self._kofferraumvolumen}"
    
class LKW(Fahrzeug):
    def __init__(self, m, b, kms, f, g):
        super().__init__(m, b, kms, f)
        self.__gewichtklasse = g
    
    def get_gewichtklasse(self):
        return self.__gewichtklasse 
    
    def __str__(self):
        return f"Fahrzeug {self._marke}: Baujahr - {self._baujahr}, km Stand - {self._km_stand}, Farbe - {self._farbe}, Gewichtklasse - {self.__gewichtklasse}t"