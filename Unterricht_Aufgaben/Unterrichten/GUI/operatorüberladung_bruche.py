# Definition der Klasse Bruch

class Bruch:
    # Definition der Konstruktor-Methode
    def __init__(self, zaehler, nenner):
        self.__zaehler = zaehler
        self.__nenner = nenner
        self.__kuerzen()
        
    def  __add__(self, other):
        z =self.__zaehler*other.__nenner + other.__zaehler*self.__nenner
        n = self.__nenner*other.__nenner
        return Bruch(z, n)  
    
    def  __sub__(self, other):
        z =self.__zaehler*other.__nenner - other.__zaehler*self.__nenner
        n = self.__nenner*other.__nenner
        return Bruch(z, n)   
    
    def  __mul__(self, other):
        z =self.__zaehler*other.__zaehler
        n = self.__nenner*other.__nenner
        return Bruch(z, n)   
    
    def  __truediv__(self, other):
        z =self.__zaehler*other.__nenner
        n = self.__nenner*other.__zaehler
        return Bruch(z, n)  
    
    def __eq__(self, other):
        return self.__zaehler == other.__zaehler and self.__nenner == other.__nenner
    
    def __kuerzen(self):
        z = self.__zaehler
        n = self.__nenner
        while n != 0:
            z, n = n, z % n
        if z > 1:
            self.__zaehler = self.__zaehler // z
            self.__nenner = self.__nenner// z
    
    
    def __str__(self):
        return f"{self.__zaehler}\n--\n{self.__nenner}" 
    
    
        
b1 = Bruch(1, 3)
b2 = Bruch(1, 3)


b = b1 + b2
print(b)

