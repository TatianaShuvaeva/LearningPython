# class Tier:
#     def __init__(self, name, alter, typ):
#         self.typ = typ
#         self.name = name
#         self.alter = alter

#     def lautgeben(self, text):
#         print(text)


# obj = Tier("Herby", 6, "Katze")
# print(obj.typ)
# obj.lautgeben("Miau")
import math

class Person:
    __alter = 42
    alter2 = 43

    def getAlter(self):
        return self.alter2
    
    def getAlter2(self) {
        x = math.sqrt(4)
        return self.__alter
    }
        

    def setAlter(self, new_alter):
        if new_alter > 100:
            raise Exception('Alter error')
        self.alter2 = new_alter


obj = Person()
print(obj.getAlter2())
# print(obj.alter2)
# print(obj.__alter)
# obj.setAlter(122)
# obj.alter2 = 122
obj.__alter = 122
# print(obj.getAlter())
print(obj.getAlter2())

