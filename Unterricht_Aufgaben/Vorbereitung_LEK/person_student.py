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
    
    def set_hat_geburstag(self):
        self.__alter += 1
        
class Student(Person):
    def __init__(self, name, vorname, alter, fachrichtung):
        super().__init__(name, vorname, alter)
        self.fachrichtung = fachrichtung
        
        
        
susi = Person("Schmidt", "Susi", 32)
susi.set_hat_geburstag()
print(susi)

benno = Student("Müller", "Benno", 29, "Maschinenbau")
print(benno)
benno.set_hat_geburstag()
print(benno)
# Zufgiffsmodifizierer
# Beschreib. Python UML
# private    __alter -
# protected  _alter  #
# public     alter   +