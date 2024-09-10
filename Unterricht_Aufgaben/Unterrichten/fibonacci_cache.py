import time
from functools import cache


@cache
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


for i in range(0, 100):
    beginn = time.time()
    fib_zahl = fibonacci_1(i)
    ende = time.time()
    print(f"Fibonacci{i:2d} = {fib_zahl:10d} in {(ende - beginn):10.4} Sek.")