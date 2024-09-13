import time
 
 
def memo(f):
    memo_dict = {}
    def helfer(x):
        if x not in memo_dict:
            memo_dict[x] = f(x)
        return memo_dict[x]
    return helfer
 
@memo
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci_1(n-1) + fibonacci_1(n-2)
 
for i in range (0, 90):
    beginn = time.time()
    fib_zahl = fibonacci_1(i)
    ende = time.time()
    print(f'Fibonacci{i:2d} = {fib_zahl:10d} in {(ende-beginn):10.4f} Sek.')