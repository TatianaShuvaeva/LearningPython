# Parameterübergabe
# args entpacken

def summe(*parameter):
    print(type(parameter))
    # print(parameter[0])
    sum = 0
    for p in parameter:
        sum += p
    return sum


s = summe()
print(f"Wert von s:{s}")

s= summe(10, 20, 50, 30, 567, 20, 70)
print(f"Wert von s:{s}")

# **kwargs
def summe_dict(**parameter):
    sum = 0
    for k, v in parameter.items():
        sum += v
    return sum

mm = {"Anton": 5, "Berti": 5, "Conni": 5, "Det": 3, "Edi": 3, "Fritzchen": 9}
s = summe_dict(**mm)
print(s)