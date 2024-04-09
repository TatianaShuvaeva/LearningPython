def rechnen(a, b=8):
    print(a*b)


def multiplizieren(a: int, *b):
    erg = a

    for i in b:
        erg *= i
    print(erg)


rechnen(2)
rechnen(3, 4)

multiplizieren('xdb')
multiplizieren(3, 5)
multiplizieren(3, 5, 7, 11)
