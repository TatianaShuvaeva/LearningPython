# OOP - Methoden

#__init__
# _str__

class Person:
    def __init__(self, name: str, vorname: str, alter: int):
        self.name = name
        self.vorname = vorname
        self.__alter = alter
    def __str__(self) -> str:
        return f"{self.vorname} {self.name} {self.__alter}"
    
    def set_hat_geburstag(self) ->:
        self.__alter += 1
        
susi = Person("Schmidt", "Susi", 32)
susi.set_hat_geburstag()
print(susi)

# Zufgiffsmodifizierer
# Beschreib. Python UML
# private    __alter -
# protected  _alter  #
# public     alter   +