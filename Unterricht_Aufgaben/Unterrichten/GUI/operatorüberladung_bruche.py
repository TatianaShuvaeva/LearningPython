# Definition der Klasse Bruch
class Bruch:
    def __init__(self, zaehler, nenner):
        if nenner == 0:
            raise ValueError("Der Nenner darf nicht 0 sein.")
        self.__zaehler = zaehler
        self.__nenner = nenner
        self.__kuerzen()

    def __add__(self, other):
        z = self.__zaehler * other.__nenner + other.__zaehler * self.__nenner
        n = self.__nenner * other.__nenner
        return Bruch(z, n)

    def __sub__(self, other):
        z = self.__zaehler * other.__nenner - other.__zaehler * self.__nenner
        n = self.__nenner * other.__nenner
        return Bruch(z, n)

    def __mul__(self, other):
        z = self.__zaehler * other.__zaehler
        n = self.__nenner * other.__nenner
        return Bruch(z, n)

    def __truediv__(self, other):
        z = self.__zaehler * other.__nenner
        n = self.__nenner * other.__zaehler
        return Bruch(z, n)

    def __eq__(self, other):
        return self.__zaehler == other.__zaehler and self.__nenner == other.__nenner

    def __kuerzen(self):
        z = abs(self.__zaehler)
        n = abs(self.__nenner)
        while n != 0:
            z, n = n, z % n
        gcd = z
        self.__zaehler //= gcd
        self.__nenner //= gcd
        if self.__nenner < 0:
            self.__zaehler = -self.__zaehler
            self.__nenner = -self.__nenner

    def __str__(self):
        if self.__nenner == 1:
            return f"{self.__zaehler}"
        return f"{self.__zaehler}\n--\n{self.__nenner}"

    def get_zaehler(self):
        return self.__zaehler

    def get_nenner(self):
        return self.__nenner

        
b1 = Bruch(1, 3)
b2 = Bruch(1, 3)


b = b1 + b2
print(b)

