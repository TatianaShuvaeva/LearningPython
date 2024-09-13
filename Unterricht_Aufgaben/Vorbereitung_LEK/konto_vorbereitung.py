class Konto:
    def __init__(self, ktnr, ktinhaber):
        self.kontonummer = ktnr
        self.kontoinhaber = ktinhaber
        self._kontosaldo = 0
    def einzahlen(self, betrag):
        self._kontosaldo += betrag
    
    def auszahlen(self, betrag):
        
        self._kontosaldo -=betrag    
        
class Girokonto(Konto):
    def __init__(self,ktnr, ktinhaber):
        super().__init__(ktnr, ktinhaber)
        
    def ueberweisen(self, other):
        pass
        
class Sparkonto(Konto):
    def __init__(self, ktnr, ktinhaber):
        super().__init__(ktnr, ktinhaber)
       
    
    def auszahlen_sparkonto(self, betrag):
        if betrag < self._kontosaldo:
            self._kontosaldo -= betrag
        else:
            return "keine Überziehung möglich"

# (Kunde) 1 -* (Girokonto)
         