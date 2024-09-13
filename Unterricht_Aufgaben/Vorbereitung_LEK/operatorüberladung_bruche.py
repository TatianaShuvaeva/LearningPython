# Operatorüberladung

class Bruch:
    def __init__(self, z, n):
        self.zaehler = z
        self.nenner = n
        
    def  __add__(self, other):
        z =self.zaehler*other.nenner + other.zaehler*self.nenner
        n = self.nenner*other.nenner
        return Bruch(z, n)   
    
    def __str__(self):
        return f"{self.zaehler}\n--\n{self.nenner}" 
    
    
        
b1 = Bruch(1, 3)
b2 = Bruch(2, 5)


b = b1 + b2
print(b)