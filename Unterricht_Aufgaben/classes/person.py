class Person:
    def __init__(self):
        self.__name = "leer"
        self.__telefon = "....."

    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n

    def get_telefon(self):
        return self.__telefon

    def set_telefon(self, n):
        self.__telefon = n

    NAME = property(get_name, set_name)
    TELEFON = property(get_telefon, set_telefon)
    
p = Person()
#print(p.__name)
print(p.get_name())

#p.__name = "Müller"
#p.set_name("Müller")
p.NAME = "Müller"
print(p.get_name())

p.TELEFON = "0123/456789"
print(p.TELEFON)