# Anonyme Funktionen mit lambda

# lambda x: x * x

print( (lambda x: x * x)(15) )

# lambda-Ausdruck einen Namen geben
q = lambda x: x * x

print ( q(12) )

f = lambda g, h: g*h

print( f(2,4))

flaeche = f(5,8)
print(flaeche)