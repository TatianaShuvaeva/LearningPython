class Fibonacci:
    def rechnen(self, n: int) -> int:
        if n == 1:
            return 1
        a = 0
        b = 1
        erg = None
        for i in range(1, n):
            erg = b + a
            a = b
            b = erg
        return erg


f = Fibonacci()
ergebnis = f.rechnen(19)
print(ergebnis)
