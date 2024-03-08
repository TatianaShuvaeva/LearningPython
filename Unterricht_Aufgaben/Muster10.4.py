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


class Person:
    __alter = 42

    def getAlter(self):
        return self.__alter


obj = Person()
print(obj.getAlter())
