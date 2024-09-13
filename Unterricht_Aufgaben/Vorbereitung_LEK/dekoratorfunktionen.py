# Dekoratorfunktion
def dekoration(funktion):
    def deko_funktion():
        print("ich bin die Dekoration")
        funktion()
    return deko_funktion

@dekoration
def normal():
    print("ich bin eine normale Funktion")



# dekoration = dekoration(normal)
normal()