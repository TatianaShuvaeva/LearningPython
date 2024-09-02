class Computer:
    def __init__(self, price):
        self.__price = price
    
    def setPrice(self, price):
        self.__price = price
    
    def getPrice(self):
        return self.__price

    
    def __str__(self):
        return f"Computer Price {self.__price}"
    

c1 = Computer(1000)
print(c1)