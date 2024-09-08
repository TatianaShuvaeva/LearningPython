class Konto:
    def __init__(self, inhaber: str, kontonummer: int, kontostand: float, max_tagesumsatz: float):
        self._umsatz: float = 0
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self._max_tagesumsatz = max_tagesumsatz

    @property
    def umsatz(self) -> float:
        return self._umsatz

    @umsatz.setter
    def umsatz(self, value: float):
        if value < 0 or value > self._max_tagesumsatz:
            raise ValueError(
                "Der Umsatz muss größer als 0, aber kleiner als der maximalen Tagesumsatz sein")
        self._umsatz = value
    
    def __eq__(self, other) -> bool:
        if self.kontonummer != other.kontonummer :
            return False
        
        if self.inhaber.lower() != other.inhaber.lower():
            return False
        
        #return True
        k1 = self.kontostand - self.umsatz
        k2 = other.kontostand - other.umsatz
        return k1 == k2
